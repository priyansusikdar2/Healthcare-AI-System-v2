const BASE_URL = "http://127.0.0.1:8000";

let isLogin = true;

function toggleMode() {
    isLogin = !isLogin;

    document.getElementById("title").innerText = isLogin ? "Login" : "Signup";

    document.querySelector("button").innerText = isLogin ? "Login" : "Signup";
}

// MAIN FUNCTION (Login + Signup)
async function login() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    if (!email || !password) {
        alert("Please fill all fields");
        return;
    }

    try {
        showLoader(true);

        let res;

        // ================= LOGIN =================
        if (isLogin) {
            const formData = new URLSearchParams();
            formData.append("username", email);  // IMPORTANT
            formData.append("password", password);

            res = await fetch(`${BASE_URL}/users/login`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded"
                },
                body: formData
            });
        }

        // ================= SIGNUP =================
        else {
            res = await fetch(`${BASE_URL}/users/signup`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    email: email,
                    password: password
                })
            });
        }

        const data = await res.json();

        if (!res.ok) {
            throw new Error(data.detail || "Something went wrong");
        }

        // ================= AFTER SUCCESS =================
        if (isLogin) {
            localStorage.setItem("token", data.access_token || data.token);
            localStorage.setItem("user", JSON.stringify(data.user || {}));

            window.location.href = "dashboard.html";
        } else {
            alert("Signup successful! Please login.");
            toggleMode();
        }

    } catch (err) {
        alert(err.message);
    } finally {
        showLoader(false);
    }
}

// LOGOUT
function logout() {
    localStorage.clear();
    window.location.href = "index.html";
}

// LOADER
function showLoader(state) {
    let loader = document.getElementById("loader");
    if (!loader) return;
    loader.style.display = state ? "block" : "none";
}
