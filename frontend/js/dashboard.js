// ================= USER =================
const user = JSON.parse(localStorage.getItem("user"));

// ================= INIT =================
document.addEventListener("DOMContentLoaded", () => {
    loadTheme();
    loadUser();
    loadRecords();
    loadChart();
    loadInsights();
});

// ================= USER =================
function loadUser() {
    if (!user || !user.username) {
        document.getElementById("userData").innerHTML = `
            <h3>👤 User</h3>
        `;
        return;
    }

    document.getElementById("userData").innerHTML = `
        <h3>👤 ${user.username}</h3>
    `;
}

// ================= STORAGE =================
function getData(key){
    return JSON.parse(localStorage.getItem(key) || "[]");
}

function saveData(key, data){
    localStorage.setItem(key, JSON.stringify(data));
}

// ================= CREATE PATIENT =================
function createPatient() {
    const name = document.getElementById("patientName").value.trim();
    const age = document.getElementById("patientAge").value.trim();

    if (!name || !age) return alert("Fill all fields");

    let patients = getData("patients");

    patients.push({ id: Date.now(), name, age });

    saveData("patients", patients);

    alert("✅ Patient created");
    loadRecords();
}

// ================= GENERIC ADD =================
function addGeneric(storageKey, inputId, field, message){
    const value = document.getElementById(inputId).value.trim();

    if (!value) return alert("Fill the field");

    let data = getData(storageKey);

    data.push({ id: Date.now(), [field]: value });

    saveData(storageKey, data);

    alert("✅ " + message);
    loadRecords();
}

// ================= ADD FUNCTIONS =================
function addFinding(){ addGeneric("findings","finding","description","Finding added"); }
function addDelivery(){ addGeneric("delivery","delivery","details","Delivery added"); }
function addEngagement(){ addGeneric("engagement","engagement","details","Engagement added"); }
function addLiteracy(){ addGeneric("literacy","literacy","details","Literacy added"); }
function addDisease(){ addGeneric("diseases","diseaseHistory","disease","Disease added"); }

// ================= LOAD RECORDS =================
function loadRecords() {

    const patients = getData("patients");
    const findings = getData("findings");
    const deliveries = getData("delivery");
    const engagements = getData("engagement");
    const literacy = getData("literacy");
    const diseases = getData("diseases");

    document.getElementById("records").innerHTML = `
        <h3>👤 Patients</h3>
        ${patients.map(p => `<div class="record-card">${p.name} (${p.age})</div>`).join("") || "<p>No patients</p>"}

        <h3>🧪 Findings</h3>
        ${findings.map(f => `<div class="record-card">${f.description}</div>`).join("") || "<p>No findings</p>"}

        <h3>🚚 Delivery</h3>
        ${deliveries.map(d => `<div class="record-card">${d.details}</div>`).join("") || "<p>No delivery</p>"}

        <h3>🤝 Engagement</h3>
        ${engagements.map(e => `<div class="record-card">${e.details}</div>`).join("") || "<p>No engagement</p>"}

        <h3>📚 Literacy</h3>
        ${literacy.map(l => `<div class="record-card">${l.details}</div>`).join("") || "<p>No literacy</p>"}

        <h3>🦠 Disease History</h3>
        ${diseases.map(d => `<div class="record-card">${d.disease}</div>`).join("") || "<p>No disease history</p>"}
    `;
}

// ================= CHART =================
function loadChart() {
    const ctx = document.getElementById("historyChart");
    if (!ctx) return;

    new Chart(ctx, {
        type: "bar",
        data: {
            labels: ["Predictions", "Patients"],
            datasets: [{
                label: "Activity",
                data: [
                    parseInt(localStorage.getItem("predictions") || 0),
                    getData("patients").length
                ]
            }]
        }
    });
}

// ================= INSIGHTS =================
function loadInsights() {
    const lastDisease = localStorage.getItem("disease") || "None";

    document.getElementById("insights").innerHTML = `
        <h3>🧠 AI Insights</h3>
        <p>Last Prediction: <b>${lastDisease}</b></p>
    `;
}

// ================= THEME =================
function toggleTheme() {
    document.body.classList.toggle("light-mode");
    localStorage.setItem(
        "theme",
        document.body.classList.contains("light-mode") ? "light" : "dark"
    );
}

function loadTheme() {
    if (localStorage.getItem("theme") === "light") {
        document.body.classList.add("light-mode");
    }
}
