from flask import Flask, render_template, request, redirect, url_for, session, flash
import base64
import pickle
import os
import io
import pickletools
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = os.urandom(16)

users_db = {}


@app.route("/")
def index():
    if "username" in session:
        return render_template("index.html", username=session["username"])
    return redirect(url_for("login"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users_db:
            flash("Username already exists!", "error")
            return redirect(url_for("register"))
        users_db[username] = generate_password_hash(password)
        flash("Registration successful!", "success")
        return redirect(url_for("index"))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users_db and check_password_hash(users_db[username], password):
            session["username"] = username
            flash("Login successful!", "success")
            return redirect(url_for("index"))
        flash("Invalid username or password!", "error")
    return render_template("login.html")


@app.route("/process", methods=["GET", "POST"])
def process():
    if "username" not in session:
        return redirect(url_for("login"))

    error = None
    disassembled_output = None

    banned_patterns = [b"\\", b"static", b"templates", b"flag.txt", b">", b"/", b"."]
    banned_instruction = "REDUCE"

    if request.method == "POST":
        payload = request.form.get("payload", "")
        try:
            decoded_data = base64.b64decode(payload)

            for pattern in banned_patterns:
                if pattern in decoded_data:
                    raise ValueError("Payload contains banned characters!")

            try:
                output = io.StringIO()
                pickletools.dis(decoded_data, out=output)
                disassembled_output = output.getvalue()

                if banned_instruction in disassembled_output:
                    raise ValueError(
                        f"Payload contains banned instruction: {banned_instruction}"
                    )

            except Exception as e:
                disassembled_output = "Error!"

            pickle.loads(decoded_data)

        except Exception as e:
            error = str(e)

    return render_template(
        "process.html", error=error, disassembled_output=disassembled_output
    )


@app.route("/logout")
def logout():
    session.pop("username", None)
    flash("Logged out successfully!", "success")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.config["SESSION_COOKIE_NAME"] = "session"
    app.run(host="0.0.0.0", port=5000, debug=True)
