const pressed = [];
const pressed2 = [];
const pressed3 = [];

const secretCode = "ArrowUpArrowUpArrowDownArrowDownArrowLeftArrowRight";
const secretCode2 = "nuitinfo";
const secretCode3 = "oo";

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
    if (pressed.join("").includes(secretCode3)) {
        img = document.createElement("img");
        img.src = "/static/assets/bubles.png";
        img.style.position = "absolute";
        window.setTimeout(() => {
            
        })
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

window.addEventListener("keyup", e => {
    pressed2.push(e.key);
    pressed2.splice(
        -secretCode2.length - 1,
        pressed2.length - secretCode2.length
    );

    if (pressed2.join("").includes(secretCode2)) {
        for(let i =0; i < 10; i++) {
            let alerte = new Audio("https://ozna.me/Metal-Gear-Alert_-Sound-Effect.mp3");
            alerte.play();
            alert("Ahah je te spam c'est drole");
        }
        
        pressed2.length = 0;
    }

});

window.addEventListener("keyup", e => {
    pressed3.push(e.key);
    pressed3.splice(
        -secretCode3.length - 1,
        pressed3.length - secretCode3.length
    );

    if (pressed3.join("").includes(secretCode3)) {
        img = document.createElement("img");
        img.src = "/static/assets/bubles.png";
        img.style.position = "absolute";
        img.style.zIndex = 10;
        var interval = window.setInterval(() => {
            console.log("ok")
            xRandom = Math.floor(Math.random() * document.querySelector("body").offsetWidth);
            yRandom = Math.floor(Math.random() * document.querySelector("body").offsetHeight);
            imgl = img;
            imgl.style.top = yRandom;
            imgl.style.left = xRandom;
            document.querySelector("body").innerHTML += `<img src="/static/assets/bubles.png" style="position:absolute;top:${yRandom};left:${xRandom};z-index:10;">`;
        }, 100);
        window.setTimeout(() => {
            window.clearInterval(interval);
        }, 5000)
    }

});