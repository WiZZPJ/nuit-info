const pressed = [];
const pressed2 = [];

const secretCode = "ArrowUpArrowUpArrowDownArrowDownArrowLeftArrowRight";
const secretCode2 = "nuitinfo";

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

});

window.addEventListener("keyup", e => {
    pressed2.push(e.key);
    pressed2.splice(
        -secretCode2.length - 1,
        pressed2.length - secretCode2.length
    );

    if (pressed2.join("").includes(secretCode2)) {
        for(let i =0; i < 10; i++) {
            let alerte = new Audio("https://ozna.me/Metal-Gear-Alert_-Sound-Effect.mp3%22");
            alerte.play();
            alert("Ahah je te spam c'est drole");
        }
        
        pressed2.length = 0;
    }

});