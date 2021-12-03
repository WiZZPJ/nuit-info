const pressed = [];

const secretCode = "ArrowUpArrowUpArrowDownArrowDownArrowLeftArrowRight";

window.addEventListener("keyup", e => {
    console.log(e.key);
    pressed.push(e.key);
    pressed.splice(
        -secretCode.length - 1,
        pressed.length - secretCode.length
    );

    if (pressed.join("").includes(secretCode)) {
        var element = document.body;
        element.classList.toggle("dark");
        if (document.body.classList.contains('dark')) {
            sessionStorage.setItem("dark", "true");
        } else {
            sessionStorage.setItem("dark", "false");
        }
        pressed.length = 0;
    }

});