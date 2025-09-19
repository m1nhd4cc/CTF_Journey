#!/usr/bin/env python3
import os
import secrets
import sys
import json


class Unbuffered(object):
    def __init__(self, stream):
        self.stream = stream

    def write(self, data):
        self.stream.write(data)
        self.stream.flush()

    def flush(self):
        self.stream.flush()

    def __getattr__(self, attr):
        return getattr(self.stream, attr)


sys.stdout = Unbuffered(sys.stdout)
sys.stderr = None

try:
    from .hashalgo import NaiveHash
except Exception:
    from hashalgo import NaiveHash

_SECRET_ENV = os.environ.get("SECRET", None)
if _SECRET_ENV is not None:
    try:
        SECRET = bytes.fromhex(_SECRET_ENV)
    except ValueError:
        SECRET = _SECRET_ENV.encode()
else:
    try:
        mn = int(os.environ.get("SECRET_LEN_MIN", "8"))
        mx = int(os.environ.get("SECRET_LEN_MAX", "32"))
        if not (1 <= mn <= mx <= 128):
            raise ValueError("invalid secret length bounds")
        sec_len = mn + secrets.randbelow(mx - mn + 1)
    except Exception:
        sec_len = 16
    SECRET = os.urandom(sec_len)

FLAG = os.environ.get("FLAG", "DDC{dummy_flag_for_local_dev}")


def mac(msg: bytes) -> bytes:
    return NaiveHash.hash(SECRET + msg)


def _log(*args):
    try:
        if getattr(sys, "stderr", None) is not None:
            print(*args, file=sys.stderr)
    except Exception:
        pass


def _bytes_info(label: str, b: bytes) -> None:
    try:
        asc = b.decode("ascii")
    except Exception:
        asc = None
    _log(f"[DBG] {label} len={len(b)} ascii={asc!r} hex={b.hex()}")


HELP_TEXT = (
    "Message signing service over TCP.\n\n"
    "Protocol: JSON per line.\n\n"
    "Commands:\n"
    '  - {"cmd":"license", "name":"alice"}\n'
    '  - {"cmd":"verify", "mac":"...", "msg":"..."}\n'
)


def parse_fields(msg_bytes) -> dict:
    if isinstance(msg_bytes, str):
        data = msg_bytes.encode("ascii", errors="ignore")
    else:
        data = bytes(msg_bytes)

    out = {}
    for part in data.split(b";"):
        if not part:
            continue
        try:
            seg = part.decode("ascii", errors="ignore")
        except Exception:
            continue
        if "=" not in seg:
            continue
        k, v = seg.split("=", 1)
        if k in ("name", "plan", "exp"):
            out[k] = v
    return out


def handle_request(req: dict) -> dict:
    cmd = (req.get("cmd") or "").strip().lower()
    if not cmd or cmd == "help":
        return {"ok": True, "help": HELP_TEXT}

    if cmd == "license":
        name = req.get("name") or "guest"
        exp = req.get("exp") or "2026-12-31"
        if not isinstance(name, str) or not isinstance(exp, str):
            return {"ok": False, "error": "name/exp must be strings"}
        msg_b = f"name={name};plan=free;exp={exp}".encode()
        tag = mac(msg_b).hex()
        _bytes_info("LICENSE msg", msg_b)
        _log(f"[DBG] LICENSE mac={tag}")
        return {
            "ok": True,
            "msg": msg_b.decode("ascii", errors="ignore"),
            "mac": tag,
        }

    if cmd == "verify":
        if "msg_hex" in req and req.get("msg_hex") is not None:
            msg_hex = req.get("msg_hex")
            if not isinstance(msg_hex, str):
                return {"ok": False, "error": "msg_hex must be hex string"}
            try:
                msg = bytes.fromhex(msg_hex)
            except ValueError:
                return {"ok": False, "error": "invalid msg_hex"}
        else:
            msg_s = req.get("msg") or ""
            if not isinstance(msg_s, str):
                return {"ok": False, "error": "msg must be a string"}
            msg = msg_s.encode()

        mac_hex = req.get("mac") or ""
        if not isinstance(mac_hex, str):
            return {"ok": False, "error": "mac must be hex string"}
        try:
            _ = bytes.fromhex(mac_hex)
        except ValueError:
            return {"ok": False, "error": "invalid mac hex"}

        _bytes_info("VERIFY msg", msg)
        _log(f"[DBG] VERIFY mac_given={mac_hex}")
        expected = mac(msg).hex()
        ok = mac_hex == expected
        _log(f"[DBG] VERIFY mac_expected={expected} match={ok}")

        fields = parse_fields(msg)
        plan = fields.get("plan", "")
        _bytes_info("VERIFY plan_field", plan.encode("ascii", errors="ignore"))

        resp = {"ok": ok, "plan": plan}
        if ok and plan in ("pro", "enterprise"):
            resp["flag"] = FLAG
        return resp

    return {"ok": False, "error": "unknown cmd"}


def main() -> int:
    rfile = sys.stdin.buffer
    wfile = sys.stdout.buffer

    hello = json.dumps({"ok": True, "hello": "License socket server"}).encode() + b"\n"
    wfile.write(hello)
    wfile.flush()

    while True:
        line = rfile.readline()
        if not line:
            break
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            if not isinstance(req, dict):
                raise ValueError("request must be a JSON object")
        except Exception as e:
            resp = {"ok": False, "error": f"invalid json: {e}"}
        else:
            try:
                resp = handle_request(req)
            except Exception as e:
                _log("[!] handler error:", e)
                resp = {"ok": False, "error": "internal error"}
        wfile.write(json.dumps(resp).encode() + b"\n")
        wfile.flush()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
