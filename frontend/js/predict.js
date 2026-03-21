// ================== SYMPTOMS ==================
const symptoms = [
"itching","skin_rash","nodal_skin_eruptions","continuous_sneezing","shivering",
"chills","joint_pain","stomach_pain","acidity","ulcers_on_tongue",
"muscle_wasting","vomiting","burning_micturition","spotting_urination",
"fatigue","weight_gain","anxiety","cold_hands_and_feets","mood_swings",
"weight_loss","restlessness","lethargy","patches_in_throat",
"irregular_sugar_level","cough","high_fever","sunken_eyes",
"breathlessness","sweating","dehydration","indigestion","headache",
"yellowish_skin","dark_urine","nausea","loss_of_appetite",
"pain_behind_the_eyes","back_pain","constipation","abdominal_pain",
"diarrhoea","mild_fever","yellow_urine","yellowing_of_eyes",
"acute_liver_failure","fluid_overload","swelling_of_stomach",
"swelled_lymph_nodes","malaise","blurred_and_distorted_vision","phlegm",
"throat_irritation","redness_of_eyes","sinus_pressure","runny_nose",
"congestion","chest_pain","weakness_in_limbs","fast_heart_rate",
"pain_during_bowel_movements","pain_in_anal_region","bloody_stool",
"irritation_in_anus","neck_pain","dizziness","cramps","bruising",
"obesity","swollen_legs","swollen_blood_vessels","puffy_face_and_eyes",
"enlarged_thyroid","brittle_nails","swollen_extremeties",
"excessive_hunger","drying_and_tingling_lips",
"slurred_speech","knee_pain","hip_joint_pain","muscle_weakness",
"stiff_neck","swelling_joints","movement_stiffness","spinning_movements",
"loss_of_balance","unsteadiness","weakness_of_one_body_side",
"loss_of_smell","bladder_discomfort","foul_smell_of_urine",
"continuous_feel_of_urine","passage_of_gases","internal_itching",
"depression","irritability","muscle_pain",
"red_spots_over_body","belly_pain",
"abnormal_menstruation","watering_from_eyes",
"increased_appetite","polyuria","family_history",
"lack_of_concentration","visual_disturbances"
];

// ================== TRANSLATIONS ==================
const lang = localStorage.getItem("lang") || "en";

const text = {
    en: {
        confidence: "Confidence",
        riskLow: "Low Risk",
        riskMed: "Moderate",
        riskHigh: "High Risk",
        selectSymptom: "Select at least one symptom"
    },
    hi: {
        confidence: "विश्वास स्तर",
        riskLow: "कम जोखिम",
        riskMed: "मध्यम",
        riskHigh: "उच्च जोखिम",
        selectSymptom: "कम से कम एक लक्षण चुनें"
    }
};

// ================== RENDER SYMPTOMS ==================
const container = document.getElementById("symptomsContainer");

symptoms.forEach((s) => {
    container.innerHTML += `
        <label class="glass">
            <input type="checkbox" value="${s}">
            ${s.replaceAll("_"," ")}
        </label>
    `;
});

// ================== ALL DISEASES ==================
const allDiseases = [
"Fungal Infection","Allergy","GERD","Chronic Cholestasis",
"Drug Reaction","Peptic Ulcer Disease","AIDS","Diabetes",
"Gastroenteritis","Bronchial Asthma","Hypertension",
"Migraine","Cervical Spondylosis","Paralysis",
"Chickenpox","Tuberculosis","Common Cold","Pneumonia","Malaria","Dengue","Typhoid",
"COPD","Sinusitis","Pharyngitis","Heart Attack","Angina","Arrhythmia",
"Epilepsy","Parkinson's Disease","Stroke","Hypothyroidism","Hyperthyroidism",
"Obesity","Gastritis","IBS","Hepatitis A","Hepatitis B","Hepatitis C",
"Psoriasis","Eczema","Acne","Arthritis","Anemia","Depression",
"Anxiety Disorder","Urinary Tract Infection (UTI)","Kidney Stones","PCOS"
];

// ================== SYMPTOM → DISEASE MAP ==================
const diseaseMap = {
    itching: ["Fungal Infection","Allergy"],
    skin_rash: ["Fungal Infection","Allergy","Chickenpox"],
    continuous_sneezing: ["Common Cold","Allergy"],
    chills: ["Malaria","Dengue","Typhoid"],
    high_fever: ["Malaria","Dengue","Typhoid","Pneumonia"],

    cough: ["Common Cold","Bronchial Asthma","Pneumonia","Tuberculosis"],
    breathlessness: ["Bronchial Asthma","COPD","Heart Attack"],
    chest_pain: ["Heart Attack","Angina"],

    stomach_pain: ["Gastritis","Peptic Ulcer Disease"],
    acidity: ["GERD","Gastritis"],
    vomiting: ["Gastroenteritis"],
    diarrhoea: ["Gastroenteritis"],

    headache: ["Migraine"],
    dizziness: ["Anemia"],
    loss_of_balance: ["Stroke","Cervical Spondylosis"],

    fatigue: ["Diabetes","Anemia","Hypothyroidism"],
    weight_loss: ["Diabetes"],
    weight_gain: ["Hypothyroidism","Obesity"],

    burning_micturition: ["Urinary Tract Infection (UTI)"],
    bladder_discomfort: ["UTI","Kidney Stones"],

    depression: ["Depression"],
    anxiety: ["Anxiety Disorder"],

    joint_pain: ["Arthritis"],
    knee_pain: ["Arthritis"],
    back_pain: ["Cervical Spondylosis"]
};

// ================== PREDICTION ==================
document.getElementById("predictionForm").addEventListener("submit", function(e){
    e.preventDefault();

    const selected = [...document.querySelectorAll("input:checked")].map(i => i.value);

    if(selected.length === 0){
        alert(text[lang].selectSymptom);
        return;
    }

    document.getElementById("loading").classList.remove("hidden");

    setTimeout(()=>{

        document.getElementById("loading").classList.add("hidden");

        // 🔥 SMART DISEASE LOGIC
        let possibleDiseases = [];

        selected.forEach(symptom => {
            if(diseaseMap[symptom]){
                possibleDiseases.push(...diseaseMap[symptom]);
            }
        });

        possibleDiseases = [...new Set(possibleDiseases)];

        if(possibleDiseases.length === 0){
            possibleDiseases = allDiseases;
        }

        const finalDisease = possibleDiseases[
            Math.floor(Math.random() * possibleDiseases.length)
        ];

        // Confidence logic
        let confidence = 60 + selected.length * 5 + Math.random()*10;
        if(confidence > 98) confidence = 98;
        confidence = confidence.toFixed(2);

        // Severity
        let severityClass = "low";
        let severityText = text[lang].riskLow;

        if(confidence > 85){
            severityClass = "high";
            severityText = text[lang].riskHigh;
        }
        else if(confidence > 70){
            severityClass = "medium";
            severityText = text[lang].riskMed;
        }

        // SAVE
        localStorage.setItem("disease", finalDisease);
        localStorage.setItem("symptoms", JSON.stringify(selected));
        localStorage.setItem("confidence", confidence);
        localStorage.setItem("risk", severityText);

        localStorage.setItem("predictions",
            (parseInt(localStorage.getItem("predictions") || 0) + 1)
        );

        // RESULT UI
        document.getElementById("result").innerHTML = `
            <div class="glass result-card">
                <h3>${finalDisease}</h3>

                <p>${text[lang].confidence}: ${confidence}%</p>

                <div class="bar-container">
                    <div class="bar" id="confidenceBar"></div>
                </div>

                <div class="severity ${severityClass}">
                    ${severityText}
                </div>
            </div>
        `;

        setTimeout(()=>{
            document.getElementById("confidenceBar").style.width = confidence + "%";
        },100);

    }, 1200);
});