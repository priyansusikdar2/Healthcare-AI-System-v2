const API_URL = "http://localhost:8000/appointments";

// ================== BOOK ==================
async function book() {
    const patient = document.getElementById("name").value.trim();
    const doctor = document.getElementById("doctor").value.trim();
    const date = document.getElementById("date").value;

    if (!patient || !doctor || !date) {
        showToast("Fill all fields ❌", true);
        return;
    }

    try {
        const res = await fetch(API_URL + "/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                patient_name: patient,
                doctor_name: doctor,
                date: new Date(date).toISOString()
            })
        });

        if (!res.ok) throw new Error();

        showToast("Booked successfully ✅");

        document.getElementById("name").value = "";
        document.getElementById("doctor").value = "";
        document.getElementById("date").value = "";

        loadAppointments();

    } catch {
        showToast("Error booking ❌", true);
    }
}


// ================== LOAD ==================
async function loadAppointments() {
    const container = document.getElementById("appointmentsList");

    const res = await fetch(API_URL + "/");
    const data = await res.json();

    if (data.length === 0) {
        container.innerHTML = "<p>No appointments</p>";
        return;
    }

    container.innerHTML = data.map(a => `
        <div class="glass appointment-card">
            <h3>${a.patient_name}</h3>
            <p>👨‍⚕️ ${a.doctor_name}</p>
            <p>📅 ${new Date(a.date).toLocaleString()}</p>
            <button onclick="deleteAppointment(${a.id})">❌ Delete</button>
        </div>
    `).join("");
}


// ================== DELETE ==================
async function deleteAppointment(id) {
    try {
        await fetch(API_URL + "/" + id, {
            method: "DELETE"
        });

        showToast("Deleted ✅");
        loadAppointments();

    } catch {
        showToast("Delete failed ❌", true);
    }
}


// ================== TOAST ==================
function showToast(msg, error=false) {
    const toast = document.createElement("div");
    toast.innerText = msg;

    toast.style.position = "fixed";
    toast.style.bottom = "20px";
    toast.style.right = "20px";
    toast.style.padding = "12px 20px";
    toast.style.borderRadius = "10px";
    toast.style.color = "white";
    toast.style.background = error ? "#ff4d4d" : "#00c853";

    document.body.appendChild(toast);
    setTimeout(() => toast.remove(), 3000);
}


// ================== INIT ==================
document.addEventListener("DOMContentLoaded", loadAppointments);
