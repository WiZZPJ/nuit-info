const pressed = [];

const secretCode = "ArrowUpArrowUpArrowDownArrowDownArrowLeftArrowRight";
const secretCode2 = "oo";

var continued = false;

window.addEventListener("keyup", e => {
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
    if (pressed.join("").includes(secretCode2)) {
        img = document.createElement("img");
        img.src = "/assets/bubles.png";
        img.style.position = "absolute";
        continued = true;
        while (continued) {
            xRandom = Math.floor(Math.random() * document.querySelector("body").offsetWidth);
            yRandom = Math.floor(Math.random() * document.querySelector("body").offsetHeight);
            imgl = img;
            imgl.style.top = yRandom;
            imgl.style.left = xRandom;
            document.appendChild(imgl);
        }
    }

});