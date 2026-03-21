// ================== UI TRANSLATIONS ==================
const translations = {
    en: {
        title: "Disease Dashboard",
        lastDisease: "Last Predicted Disease",
        symptoms: "Selected Symptoms",
        risk: "Risk Level",
        activity: "Recent Activity",

        total: "Total Predictions",
        accuracy: "Accuracy",
        users: "Users",

        low: "Low",
        medium: "Moderate",
        high: "High",

        none: "None",
        notPredicted: "Not predicted",

        viewedDashboard: "Viewed dashboard",
        checkedSymptoms: "Checked symptoms",
        viewedPrediction: "Viewed prediction",
        usedChatbot: "Used chatbot"
    },

    hi: {
        title: "रोग डैशबोर्ड",
        lastDisease: "अंतिम अनुमानित रोग",
        symptoms: "चयनित लक्षण",
        risk: "जोखिम स्तर",
        activity: "हाल की गतिविधि",

        total: "कुल भविष्यवाणियाँ",
        accuracy: "सटीकता",
        users: "उपयोगकर्ता",

        low: "कम",
        medium: "मध्यम",
        high: "उच्च",

        none: "कोई नहीं",
        notPredicted: "कोई अनुमान नहीं",

        viewedDashboard: "डैशबोर्ड देखा",
        checkedSymptoms: "लक्षण जांचे",
        viewedPrediction: "पूर्वानुमान देखा",
        usedChatbot: "चैटबॉट उपयोग किया"
    }
};

// ================== DISEASE TRANSLATIONS ==================
const diseaseMap = {
  "Fungal Infection": "फंगल संक्रमण",
  "Allergy": "एलर्जी",
  "GERD": "गैस्ट्रोएसोफेगल रिफ्लक्स रोग",
  "Chronic Cholestasis": "दीर्घकालिक पित्त रुकावट",

  "Drug Reaction": "दवा की प्रतिक्रिया",
  "Peptic Ulcer Disease": "पेप्टिक अल्सर रोग",
  "AIDS": "एड्स",
  "Diabetes": "मधुमेह",

  "Gastroenteritis": "आंत्रशोथ",
  "Bronchial Asthma": "ब्रोंकियल अस्थमा",
  "Hypertension": "उच्च रक्तचाप",

  "Migraine": "माइग्रेन",
  "Cervical Spondylosis": "गर्दन की स्पॉन्डिलोसिस",
  "Paralysis": "लकवा",

  "Chickenpox": "चेचक",
  "Tuberculosis": "तपेदिक",
  "Common Cold": "सामान्य सर्दी",
  "Pneumonia": "निमोनिया",
  "Malaria": "मलेरिया",
  "Dengue": "डेंगू",
  "Typhoid": "टाइफाइड",

  "COPD": "क्रॉनिक ऑब्सट्रक्टिव पल्मोनरी डिजीज",
  "Sinusitis": "साइनसाइटिस",
  "Pharyngitis": "गले की सूजन",
  "Heart Attack": "दिल का दौरा",
  "Angina": "एंजाइना",
  "Arrhythmia": "हृदय की अनियमित धड़कन",

  "Epilepsy": "मिर्गी",
  "Parkinson's Disease": "पार्किंसन रोग",
  "Stroke": "स्ट्रोक",
  "Hypothyroidism": "हाइपोथायरायडिज्म",
  "Hyperthyroidism": "हाइपरथायरायडिज्म",

  "Obesity": "मोटापा",
  "Gastritis": "गैस्ट्राइटिस",
  "IBS": "इर्रिटेबल बाउल सिंड्रोम",
  "Hepatitis A": "हेपेटाइटिस ए",
  "Hepatitis B": "हेपेटाइटिस बी",
  "Hepatitis C": "हेपेटाइटिस सी",

  "Psoriasis": "सोरायसिस",
  "Eczema": "एक्जिमा",
  "Acne": "मुंहासे",
  "Arthritis": "गठिया",
  "Anemia": "एनीमिया",
  "Depression": "अवसाद",

  "Anxiety Disorder": "चिंता विकार",
  "Urinary Tract Infection (UTI)": "मूत्र मार्ग संक्रमण",
  "Kidney Stones": "गुर्दे की पथरी",
  "PCOS": "पॉलीसिस्टिक ओवरी सिंड्रोम"
};
// ================== SYMPTOM TRANSLATIONS ==================
const symptomMap = {
"itching":"खुजली",
"skin_rash":"त्वचा पर चकत्ते",
"nodal_skin_eruptions":"त्वचा पर गांठदार फुंसियाँ",
"continuous_sneezing":"लगातार छींक आना",
"shivering":"कंपकंपी",
"chills":"ठंड लगना",
"joint_pain":"जोड़ों का दर्द",
"stomach_pain":"पेट दर्द",
"acidity":"अम्लता / एसिडिटी",
"ulcers_on_tongue":"जीभ पर छाले",

"muscle_wasting":"मांसपेशियों का क्षय",
"vomiting":"उल्टी",
"burning_micturition":"पेशाब में जलन",
"spotting_urination":"पेशाब में खून की बूंदें",
"fatigue":"थकान",
"weight_gain":"वजन बढ़ना",
"anxiety":"चिंता",
"cold_hands_and_feets":"हाथ-पैर ठंडे होना",
"mood_swings":"मन का बार-बार बदलना",

"weight_loss":"वजन कम होना",
"restlessness":"बेचैनी",
"lethargy":"सुस्ती",
"patches_in_throat":"गले में धब्बे",
"irregular_sugar_level":"अनियमित शुगर स्तर",
"cough":"खांसी",
"high_fever":"तेज बुखार",
"sunken_eyes":"धंसी हुई आंखें",

"breathlessness":"सांस फूलना",
"sweating":"पसीना आना",
"dehydration":"निर्जलीकरण",
"indigestion":"अपच",
"headache":"सिरदर्द",
"yellowish_skin":"त्वचा का पीला पड़ना",
"dark_urine":"गहरे रंग का पेशाब",
"nausea":"मितली",
"loss_of_appetite":"भूख न लगना",

"pain_behind_the_eyes":"आंखों के पीछे दर्द",
"back_pain":"पीठ दर्द",
"constipation":"कब्ज",
"abdominal_pain":"पेट में दर्द",
"diarrhoea":"दस्त",
"mild_fever":"हल्का बुखार",
"yellow_urine":"पीला पेशाब",
"yellowing_of_eyes":"आंखों का पीला पड़ना"
};

// ================== CURRENT LANG ==================
let currentLang = localStorage.getItem("lang") || "en";

// ================== GLOBAL TEXT ==================
function t(key) {
    return translations[currentLang][key] || key;
}

// ================== TRANSLATE DISEASE ==================
function translateDisease(disease) {
    if (currentLang === "hi") {
        return diseaseMap[disease] || disease;
    }
    return disease;
}

// ================== TRANSLATE SYMPTOMS ==================
function translateSymptoms(symptomsArray) {
    if (currentLang === "hi") {
        return symptomsArray.map(s => symptomMap[s] || s.replaceAll("_", " "));
    }
    return symptomsArray.map(s => s.replaceAll("_", " "));
}

// ================== LANGUAGE SWITCH ==================
function setLanguage(lang) {
    currentLang = lang;
    localStorage.setItem("lang", lang);
    location.reload();
}

// ================== APPLY STATIC TEXT ==================
function applyTranslations() {
    document.querySelectorAll("[data-i18n]").forEach(el => {
        const key = el.getAttribute("data-i18n");
        el.innerText = t(key);
    });
}

// ================== INIT ==================
document.addEventListener("DOMContentLoaded", applyTranslations);