const pressed = [];

const secretCode = "ArrowUpArrowUpArrowDownArrowDownArrowLeftArrowRight";
const secretCode2 = "jesuisunelicorne";

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
    pressed.push(e.key);
    pressed.splice(
        -secretCode2.length - 1,
        pressed.length - secretCode2.length
    );

    if (pressed.join("").includes(secretCode2)) {
        for(let i =0; i < 10; i++) {
            alert("Ahah je te spam c'est drole");
        }
        
        pressed.length = 0;
    }

});