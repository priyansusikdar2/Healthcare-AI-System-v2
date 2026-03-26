const BASE_URL = "http://127.0.0.1:8000";
const token = localStorage.getItem("token");

// ✅ CORRECT ENDPOINT (from main.py)
const PREDICT_API = "/ml/predict";

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

// ================== HELPER ==================
function el(id){
    return document.getElementById(id);
}

// ================== RENDER SYMPTOMS ==================
const container = el("symptomsContainer");

if (container) {
    container.innerHTML = symptoms.map(s => `
        <label class="glass">
            <input type="checkbox" value="${s}">
            ${s.replaceAll("_"," ")}
        </label>
    `).join("");
}

// ================== FORM SUBMIT ==================
const form = el("predictionForm");

if (form) {
    form.addEventListener("submit", async function(e){
        e.preventDefault();

        const selected = [...document.querySelectorAll("input:checked")]
            .map(i => i.value);

        if (selected.length === 0) {
            alert("⚠️ Select at least one symptom");
            return;
        }

        // ================== CREATE FEATURE VECTOR ==================
        let featureVector = {};

        symptoms.forEach(symptom => {
            featureVector[symptom] = selected.includes(symptom) ? 1 : 0;
        });

        try {
            console.log("🚀 Sending request to:", BASE_URL + PREDICT_API);
            console.log("📦 Payload:", featureVector);

            const res = await fetch(BASE_URL + PREDICT_API, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    ...(token && { "Authorization": `Bearer ${token}` })
                },
                body: JSON.stringify({
                    data: featureVector   // ✅ IMPORTANT FIX
                })
            });

            const data = await res.json();
            console.log("✅ Backend Response:", data);

            // ================== ERROR HANDLING ==================
            if (!res.ok || data.error) {
                console.error("❌ FULL ERROR:", data);
                throw new Error(data.error || "Prediction failed");
            }

            const disease = data.prediction || "Unknown";
            const confidence = data.confidence || 0;

            // ================== SAVE ==================
            localStorage.setItem("disease", disease);
            localStorage.setItem("confidence", confidence);

            localStorage.setItem(
                "predictions",
                (parseInt(localStorage.getItem("predictions") || 0) + 1)
            );

            // ================== UI ==================
            el("result").innerHTML = `
                <div class="glass result-card">
                    <h3>🩺 ${disease}</h3>
                    <p>Confidence: ${confidence}%</p>
                </div>
            `;

        } catch (err) {
            console.error("🔥 Prediction Error:", err);

            el("result").innerHTML = `
                <p style="color:red;">❌ ${err.message}</p>
            `;
        }
    });
}
