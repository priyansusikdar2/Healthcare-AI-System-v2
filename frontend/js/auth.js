function login(){
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    if(username === "" || password === ""){
        alert("Enter username and password");
        return;
    }

    localStorage.setItem("user", username);
    alert("Login successful!");

    window.location.href = "dashboard.html";
}