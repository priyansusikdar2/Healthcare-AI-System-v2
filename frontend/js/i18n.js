const translations = {
    en: {
        dashboard: "Patient Dashboard",
        predict: "Prediction",
        appointment: "Appointment",
        logout: "Logout"
    },
    hi: {
        dashboard: "रोगी डैशबोर्ड",
        predict: "पूर्वानुमान",
        appointment: "अपॉइंटमेंट",
        logout: "लॉगआउट"
    }
};

// ================= APPLY LANGUAGE =================
function applyLang(lang) {
    localStorage.setItem("lang", lang);

    document.querySelectorAll("[data-i18n]").forEach(el => {
        const key = el.getAttribute("data-i18n");
        if (translations[lang][key]) {
            el.innerText = translations[lang][key];
        }
    });
}

// ================= CHANGE LANG =================
function changeLang(lang) {
    applyLang(lang);
}

// ================= INIT =================
document.addEventListener("DOMContentLoaded", () => {
    const lang = localStorage.getItem("lang") || "en";
    applyLang(lang);
});
