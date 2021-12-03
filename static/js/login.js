/**
 * Create a dialog box in the web page to inform the user of activity
 * @param {string} type Type of message (error, success, warning)
 * @param {string} message Message to display
 */
function create_alert(type, message) {
    let alertBanner = document.createElement('div');
    alertBanner.classList.add("alert", type);
    alertBanner.textContent = message;
    document.body.appendChild(alertBanner);
    let clear = setTimeout(() => {
        document.body.removeChild(alertBanner);
    }, 4000);
    alertBanner.onclick = () => {
        document.body.removeChild(alertBanner);
        clearTimeout(clear);
    };
}



let form = document.querySelector('form');
form.onsubmit = (e) => {
    e.preventDefault();
    let data = {};
    console.log(form);

    form.querySelectorAll('input[name]').forEach(elem => {
        data[elem.name] = elem.value;
    });

    let payload = new FormData();
    payload.append( "json", JSON.stringify(data));

    fetch('/api/v1/auth', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: payload
    }).then(async data => {
        if (data.status === 200) {
            create_alert('success', "Connexion réussie");
            setTimeout(() => {
                location = "https://nuit.ozna.me/";
            }, 250);

        } else if (/(50*)|404|418/.test(String(data.status))) {
            create_alert('error', "Identifiants incorrects")
        }
    });
};
