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
        document.querySelector("body").style.position = "relative";
        img = document.createElement("img");
        img.src = "/static/assets/bubles.png";
        img.style.position = "absolute";
        img.style.zIndex = 10;
        var interval = window.setInterval(() => {
            console.log("ok")
            xRandom = Math.floor(Math.random() * window.screen.width);
            yRandom = Math.floor(Math.random() * window.screen.height);
            imgl = img;
            imgl.style.top = yRandom;
            imgl.style.left = xRandom;
            imgl.style.opacity = Math.random();
            var id = Math.floor(Math.random() * 1000);
            document.querySelector(".bodyContainer").innerHTML += `<img id="bubles-${id}" class="bubles" src="/static/assets/bubles.png" style="opacity:${Math.random()};position:absolute;top:${yRandom}px;left:${xRandom}px;z-index:10;">`;
            window.setTimeout(() => {
                document.getElementById("bubles-" + id).remove();
            }, 10000)
        }, 100);
        window.setTimeout(() => {
            window.clearInterval(interval);
        }, 10000)
    }

});

var img = document.querySelector('img[name=poisson]');

img.onclick = function() {
    let alerte_pnj = new Audio("/static/son/pnj.mp3");
    alerte_pnj.play();
}
