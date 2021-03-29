document.addEventListener("DOMContentLoaded", () => {
    let led = document.getElementById('ledbutton')
    led.addEventListener('click', () => fetch('/led'))
})

window.onload = loadStyleSheet;

function loadStyleSheet() {
    if (document.cookie === "darkmode=true") {
        setDarkMode();
    } else {
        setLightMode();
    }
}
function setDarkMode() {

    document.cookie = "darkmode=true";
    document.getElementById("modet").removeAttribute("checked");
    document.getElementById("mode").setAttribute('href', "/static/css/spectre.min.css");
    document.getElementById("mode2").setAttribute('href', "/static/css/spectre-exp.min.css");
    document.getElementById("mode3").setAttribute('href', "/static/css/spectre-icons.min.css");
     
}
function setLightMode() {
    document.getElementById("modet").setAttribute('checked', "")
    document.cookie = "darkmode=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    document.getElementById("mode").setAttribute('href', 'https://unpkg.com/spectre.css/dist/spectre.min.css');
    document.getElementById("mode2").setAttribute('href', "https://unpkg.com/spectre.css/dist/spectre-exp.min.css");
    document.getElementById("mode3").setAttribute('href', "https://unpkg.com/spectre.css/dist/spectre-icons.min.css");
}

document.addEventListener("DOMContentLoaded", function (event) {
    var _selector = document.querySelector('input[name=checkbox]');
    _selector.addEventListener('change', function (event) {
        if (_selector.checked) {
            setLightMode();
        } else {
            setDarkMode();
        }
    });
});
