// ================== LOAD DASHBOARD ==================
function loadDashboard() {

    const lang = localStorage.getItem("lang") || "en";

    // ================== DATA ==================
    const rawDisease = localStorage.getItem("disease") || t("notPredicted");
    const rawSymptoms = JSON.parse(localStorage.getItem("symptoms") || "[]");
    const rawRisk = localStorage.getItem("risk") || "Low";

    const totalPredictions = parseInt(localStorage.getItem("predictions") || "0");

    // ================== STATS ==================
    const accuracy = "92%";
    const users = 1000 + totalPredictions * 5;

    // ================== TRANSLATION ==================
    const disease = translateDisease(rawDisease);
    const symptoms = rawSymptoms.length
        ? translateSymptoms(rawSymptoms)
        : [t("none")];

    const risk = translateRisk(rawRisk);

    // ================== RENDER ==================
    document.getElementById("disease").innerText = disease;

    document.getElementById("symptoms").innerText =
        symptoms.join(", ");

    document.getElementById("risk").innerText = risk;

    document.getElementById("totalPredictions").innerText = totalPredictions;
    document.getElementById("accuracy").innerText = accuracy;
    document.getElementById("users").innerText = users.toLocaleString();

    // ================== ACTIVITY ==================
    loadActivity();

    // ================== SAVE ACTIVITY ==================
    saveActivity(t("viewedDashboard"));
}

// ================== TRANSLATE RISK ==================
function translateRisk(risk) {

    const r = risk.toLowerCase();

    if (r.includes("low")) return t("low");
    if (r.includes("moderate") || r.includes("medium")) return t("medium");
    if (r.includes("high")) return t("high");

    return risk;
}

// ================== SAVE ACTIVITY ==================
function saveActivity(action) {

    let activities = JSON.parse(localStorage.getItem("activities") || "[]");

    const time = new Date().toLocaleTimeString();

    activities.unshift(`${action} (${time})`);

    // keep only last 5
    activities = activities.slice(0, 5);

    localStorage.setItem("activities", JSON.stringify(activities));
}

// ================== LOAD ACTIVITY ==================
function loadActivity() {

    const list = document.getElementById("activity-list");

    let activities = JSON.parse(localStorage.getItem("activities") || "[]");

    // Default activity if empty
    if (activities.length === 0) {
        activities = [
            t("checkedSymptoms"),
            t("viewedPrediction"),
            t("usedChatbot")
        ];
    }

    list.innerHTML = "";

    activities.forEach(a => {
        const li = document.createElement("li");
        li.innerText = a;
        list.appendChild(li);
    });
}

// ================== INIT ==================
document.addEventListener("DOMContentLoaded", () => {

    // Apply UI translations first
    if (typeof applyTranslations === "function") {
        applyTranslations();
    }

    // Load dynamic dashboard data
    loadDashboard();
});