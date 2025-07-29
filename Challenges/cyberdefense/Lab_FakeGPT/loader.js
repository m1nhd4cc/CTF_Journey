(function() {
    var _0xabc1 = function(_0x321a) {
        return _0x321a;
    };
    // Check if the browser is in a virtual environment
    if (navigator.plugins.length === 0 || /HeadlessChrome/.test(navigator.userAgent)) {
        alert("Virtual environment detected. Extension will disable itself.");
        chrome.runtime.onMessage.addListener(() => { return false; });
    }

    // Load additional scripts dynamically
    function loadScript(url, callback) {
        var script = document.createElement('script');
        script.src = url;
        script.onload = callback;
        document.head.appendChild(script);
    }

    // Load and execute the core functionality
    loadScript('core/app.js', function() {
        console.log('Core functionality loaded.');
    });
})();
