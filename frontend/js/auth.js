// Base API URL (change if deployed)
const API_BASE = "http://127.0.0.1:8000";

// =========================
// 🔐 LOGIN FUNCTION
// =========================
async function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    if (username === "" || password === "") {
        alert("Enter username and password");
        return;
    }

    try {
        const response = await fetch(`${API_BASE}/users/login`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username: username,
                password: password
            })
        });

        const data = await response.json();

        if (!response.ok) {
            alert(data.detail || "Login failed");
            return;
        }

        // ✅ Store token
        localStorage.setItem("token", data.access_token);
        localStorage.setItem("user", username);

        alert("Login successful!");

        // Redirect to dashboard
        window.location.href = "dashboard.html";

    } catch (error) {
        console.error("Login error:", error);
        alert("Server error. Try again later.");
    }
}


// =========================
// 📝 SIGNUP FUNCTION
// =========================
async function signup() {
    const username = document.getElementById("username").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    if (username === "" || email === "" || password === "") {
        alert("All fields are required");
        return;
    }

    try {
        const response = await fetch(`${API_BASE}/users/register`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username: username,
                email: email,
                password: password
            })
        });

        const data = await response.json();

        if (!response.ok) {
            alert(data.detail || "Signup failed");
            return;
        }

        alert("Signup successful! Please login.");
        window.location.href = "login.html";

    } catch (error) {
        console.error("Signup error:", error);
        alert("Server error. Try again later.");
    }
}


// =========================
// 🔓 LOGOUT FUNCTION
// =========================
function logout() {
    localStorage.removeItem("token");
    localStorage.removeItem("user");

    alert("Logged out successfully");
    window.location.href = "login.html";
}


// =========================
// 🔒 CHECK AUTH (PROTECT PAGES)
// =========================
function checkAuth() {
    const token = localStorage.getItem("token");

    if (!token) {
        alert("Please login first!");
        window.location.href = "login.html";
    }
}


// =========================
// 👤 GET CURRENT USER (OPTIONAL)
// =========================
async function getCurrentUser() {
    const token = localStorage.getItem("token");

    try {
        const response = await fetch(`${API_BASE}/users/me`, {
            headers: {
                "Authorization": `Bearer ${token}`
            }
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error("Unauthorized");
        }

        return data;

    } catch (error) {
        console.error("Auth error:", error);
        logout();
    }
}