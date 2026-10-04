# import streamlit as st
# import pandas as pd
# import joblib

# # Load saved model, scaler, and expected columns
# model = joblib.load("logistic_regression_model.pkl")
# scaler = joblib.load("scaler.pkl")
# expected_columns = joblib.load("heart_columns.pkl")

# st.title("Heart Stroke Prediction")
# st.markdown("Provide the following details to check your heart stroke risk:")

# # Collect user input
# age = st.slider("Age", 18, 100, 40)
# sex = st.selectbox("Sex", ["M", "F"])
# chest_pain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"])
# resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
# cholesterol = st.number_input("Cholesterol (mg/dL)", 100, 600, 200)
# fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", [0, 1])
# resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
# max_hr = st.slider("Max Heart Rate", 60, 220, 150)
# exercise_angina = st.selectbox("Exercise-Induced Angina", ["Y", "N"])
# oldpeak = st.slider("Oldpeak (ST Depression)", 0.0, 6.0, 1.0)
# st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

# # When Predict is clicked
# if st.button("Predict"):

#     # Create a raw input dictionary
#     raw_input = {
#         'Age': age,
#         'RestingBP': resting_bp,
#         'Cholesterol': cholesterol,
#         'FastingBS': fasting_bs,
#         'MaxHR': max_hr,
#         'Oldpeak': oldpeak,
#         'Sex_' + sex: 1,
#         'ChestPainType_' + chest_pain: 1,
#         'RestingECG_' + resting_ecg: 1,
#         'ExerciseAngina_' + exercise_angina: 1,
#         'ST_Slope_' + st_slope: 1
#     }

#     # Create input dataframe
#     input_df = pd.DataFrame([raw_input])

#     # Fill in missing columns with 0s
#     for col in expected_columns:
#         if col not in input_df.columns:
#             input_df[col] = 0

#     # Reorder columns
#     input_df = input_df[expected_columns]

#     # Scale the input
#     # scaled_input = scaler.transform(input_df)

#     # Make prediction
#     # prediction = model.predict(scaled_input)[0]
#     prediction = model.predict(input_df)[0]

#     # Show result
#     if prediction == 1:
#         st.error("⚠️ High Risk of Heart Disease")
#     else:
#         st.success("✅ Low Risk of Heart Disease")


import streamlit as st
import pandas as pd
import joblib

# --------------------------------------------------
# Load trained model and feature information
# --------------------------------------------------

model = joblib.load("logistic_regression_model.pkl")
expected_columns = joblib.load("heart_columns.pkl")

# If your Logistic Regression model was trained using
# scaled data, also load the scaler:
# scaler = joblib.load("scaler.pkl")


# --------------------------------------------------
# Page configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="centered"
)

st.title("❤️ Heart Disease Prediction")
st.markdown(
    "Enter the patient's details below to predict the risk of heart disease."
)


# --------------------------------------------------
# Prediction Form
# --------------------------------------------------

with st.form("heart_prediction_form"):

    st.subheader("Patient Information")

    age = st.slider(
        "Age",
        min_value=18,
        max_value=100,
        value=40
    )

    sex = st.selectbox(
        "Sex",
        ["M", "F"]
    )

    chest_pain = st.selectbox(
        "Chest Pain Type",
        ["ATA", "NAP", "TA", "ASY"]
    )

    resting_bp = st.number_input(
        "Resting Blood Pressure (mm Hg)",
        min_value=80,
        max_value=200,
        value=120
    )

    cholesterol = st.number_input(
        "Cholesterol (mg/dL)",
        min_value=100,
        max_value=600,
        value=200
    )

    fasting_bs = st.selectbox(
        "Fasting Blood Sugar > 120 mg/dL",
        [0, 1]
    )

    resting_ecg = st.selectbox(
        "Resting ECG",
        ["Normal", "ST", "LVH"]
    )

    max_hr = st.slider(
        "Maximum Heart Rate",
        min_value=60,
        max_value=220,
        value=150
    )

    exercise_angina = st.selectbox(
        "Exercise-Induced Angina",
        ["Y", "N"]
    )

    oldpeak = st.slider(
        "Oldpeak (ST Depression)",
        min_value=0.0,
        max_value=6.0,
        value=1.0,
        step=0.1
    )

    st_slope = st.selectbox(
        "ST Slope",
        ["Up", "Flat", "Down"]
    )

    # Submit button
    predict_button = st.form_submit_button(
        "🔍 Predict"
    )


# --------------------------------------------------
# Prediction
# --------------------------------------------------

if predict_button:

    # Create input dictionary
    raw_input = {
        "Age": age,
        "RestingBP": resting_bp,
        "Cholesterol": cholesterol,
        "FastingBS": fasting_bs,
        "MaxHR": max_hr,
        "Oldpeak": oldpeak,

        "Sex_" + sex: 1,

        "ChestPainType_" + chest_pain: 1,

        "RestingECG_" + resting_ecg: 1,

        "ExerciseAngina_" + exercise_angina: 1,

        "ST_Slope_" + st_slope: 1
    }

    # Convert to DataFrame
    input_df = pd.DataFrame([raw_input])

    # Add missing columns
    for col in expected_columns:

        if col not in input_df.columns:
            input_df[col] = 0

    # Keep exactly the same column order
    # as used during model training
    input_df = input_df[expected_columns]


    # --------------------------------------------------
    # Prediction
    # --------------------------------------------------

    prediction = model.predict(input_df)[0]


    # --------------------------------------------------
    # Display result
    # --------------------------------------------------

    st.divider()

    if prediction == 1:

        st.error(
            "⚠️ High Risk of Heart Disease"
        )

    else:

        st.success(
            "✅ Low Risk of Heart Disease"
        )