function sendMsg(){
    let msg = document.getElementById("msg").value;
    document.getElementById("chat").innerHTML += `<p>You: ${msg}</p>`;
    document.getElementById("chat").innerHTML += `<p>Bot: Stay hydrated!</p>`;
}