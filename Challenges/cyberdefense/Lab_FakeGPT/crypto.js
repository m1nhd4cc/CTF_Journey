(function() {
    window.CryptoUtils = {
        encrypt: function(data) {
            const key = CryptoJS.enc.Utf8.parse('SuperSecretKey123');
            const iv = CryptoJS.lib.WordArray.random(16);
            const encrypted = CryptoJS.AES.encrypt(data, key, { iv: iv });
            return encrypted.toString(CryptoJS.enc.Base64);
        }
    };
})();
