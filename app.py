# import streamlit as st
# import pandas as pd
# import numpy as np
# import joblib
# import os

# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(
#     page_title="Water Quality Evaluation",
#     layout="wide"
# )

# st.title("💧 Water Quality Evaluation System")

# # ---------------- LOAD MODEL FILES ----------------

# @st.cache_resource
# def load_artifacts():
#     model = joblib.load("water_potability_rf_model.pkl")
#     scaler = joblib.load("scaler.pkl")
#     features = joblib.load("features.pkl")
#     return model, scaler, features


# # Error-safe loading
# try:
#     model, scaler, features = load_artifacts()
# except Exception as e:
#     st.error("❌ Error loading model files. Make sure all .pkl files exist.")
#     st.stop()

# # ---------------- SIDEBAR INPUT ----------------
# st.sidebar.title("🧪 Enter Water Parameters")

# ph = st.sidebar.slider("pH", 0.0, 14.0, 7.0, 0.01)
# hardness = st.sidebar.slider("Hardness", 0.0, 350.0, 120.0)
# solids = st.sidebar.slider("Solids (mg/L)", 0.0, 30000.0, 3000.0)
# chloramines = st.sidebar.slider("Chloramines", 0.0, 15.0, 7.0)
# sulfate = st.sidebar.slider("Sulfate (mg/L)", 0.0, 500.0, 330.0)
# conductivity = st.sidebar.slider("Conductivity (µS/cm)", 0.0, 800.0, 420.0)
# organic_carbon = st.sidebar.slider("Organic Carbon (mg/L)", 0.0, 30.0, 10.0)
# trihalomethanes = st.sidebar.slider("Trihalomethanes", 0.0, 150.0, 65.0)
# turbidity = st.sidebar.slider("Turbidity (NTU)", 0.0, 10.0, 4.0)

# # ---------------- INPUT DATAFRAME ----------------
# input_dict = {
#     "ph": ph,
#     "Hardness": hardness,
#     "Solids": solids,
#     "Chloramines": chloramines,
#     "Sulfate": sulfate,
#     "Conductivity": conductivity,
#     "Organic_carbon": organic_carbon,
#     "Trihalomethanes": trihalomethanes,
#     "Turbidity": turbidity
# }

# input_df = pd.DataFrame([input_dict])

# # Ensure correct feature order
# input_df = input_df[features]

# st.subheader("📋 Selected Input Values")
# st.dataframe(input_df)

# # ---------------- PREDICTION ----------------
# if st.button("🔍 Predict Water Quality"):
#     input_scaled = scaler.transform(input_df)
#     prediction = model.predict(input_scaled)

#     st.divider()
#     st.subheader("📊 Prediction Result")

#     if prediction[0] == 1:
#         st.success("✅ Water is **SAFE** to drink")
#     else:
#         st.error("❌ Water is **NOT SAFE** to drink")

# # ---------------- TREATMENT RECOMMENDATIONS ----------------
# st.divider()
# st.header("🛠️ Treatment Recommendations")

# with st.expander("View Suggested Treatments", expanded=True):
#     col1, col2 = st.columns(2)

#     with col1:
#         st.markdown("### Physical Treatment")
#         if turbidity > 5:
#             st.write("- High turbidity → **Coagulation & Filtration**")
#         if solids > 1000:
#             st.write("- High solids → **Reverse Osmosis (RO)**")
#         st.write("- Basic filtration recommended")

#     with col2:
#         st.markdown("### Chemical / Biological")
#         if ph < 6.5 or ph > 8.5:
#             st.write("- pH imbalance → **Neutralization required**")
#         st.write("- **UV / Chlorination** for disinfection")

# st.info("💡 Always consult local water authorities for drinking standards.")







# 2nd code


# import streamlit as st
# import pandas as pd
# import joblib

# # ---------------- PAGE CONFIG ----------------
# st.set_page_config(
#     page_title="HYDRO-INFORMATICS SYSTEM",
#     layout="wide"
# )

# st.title("HYDRO-INFORMATICS SYSTEM")

# # ---------------- LOAD MODEL FILES ----------------
# @st.cache_resource
# def load_artifacts():
#     model = joblib.load("water_potability_rf_model.pkl")
#     scaler = joblib.load("scaler.pkl")
#     features = joblib.load("features.pkl")
#     return model, scaler, features

# try:
#     model, scaler, features = load_artifacts()
# except Exception:
#     st.error("Error loading model files. Make sure all .pkl files exist in the same folder.")
#     st.stop()

# # ---------------- FUNCTIONS ----------------
# def assign_usecases(row):
#     usecases = []

#     if 6.5 <= row['ph'] <= 8.5 and row['Turbidity'] <= 5 and row['Trihalomethanes'] <= 0.1 and row['Sulfate'] <= 400:
#         usecases.append("Drinking Water")

#     if row['Hardness'] <= 500 and row['Solids'] <= 500:
#         usecases.append("Domestic Use (washing, cleaning)")

#     if row['Sulfate'] <= 400 and row['Conductivity'] <= 1000:
#         usecases.append("Agricultural Use")

#     if row['Conductivity'] <= 1500 and row['Turbidity'] <= 10:
#         usecases.append("Energy Production (cooling / hydropower)")

#     if row['Chloramines'] >= 0.2 and row['Turbidity'] <= 5:
#         usecases.append("Public & Municipal Use")

#     if row['Organic_carbon'] <= 10 and row['Trihalomethanes'] <= 0.1:
#         usecases.append("Medical & Scientific Uses (Strict Quality)")

#     return "; ".join(usecases) if usecases else "Not recommended for standard use"


# def recommend_treatment(row):
#     recommendations = []

#     if row['ph'] < 6.5:
#         recommendations.append("pH is acidic → Lime / alkaline treatment required")
#     elif row['ph'] > 8.5:
#         recommendations.append("pH is basic → Acid dosing for correction")

#     if row['Hardness'] > 500:
#         recommendations.append("High hardness → Ion exchange or lime-soda softening")

#     if row['Solids'] > 500:
#         recommendations.append("High solids → Sedimentation and filtration")

#     if row['Chloramines'] < 0.2:
#         recommendations.append("Low disinfectant → Add chlorination")
#     elif row['Chloramines'] > 2:
#         recommendations.append("Excess chloramines → Dechlorination required")

#     if row['Sulfate'] > 400:
#         recommendations.append("High sulfate → Reverse Osmosis / Ion Exchange")

#     if row['Conductivity'] > 1000:
#         recommendations.append("High salinity → Desalination (RO)")

#     if row['Organic_carbon'] > 10:
#         recommendations.append("High organic carbon → Activated carbon / AOP")

#     if row['Trihalomethanes'] > 0.1:
#         recommendations.append("High THMs → Reduce chlorination / precursor removal")

#     if row['Turbidity'] > 5:
#         recommendations.append("High turbidity → Filtration and sedimentation")

#     return "; ".join(recommendations) if recommendations else "Water within acceptable limits"

# # ---------------- SIDEBAR INPUT ----------------
# st.sidebar.title("Enter Water Parameters")

# ph = st.sidebar.slider("pH", 0.0, 14.0, 7.0, 0.01)
# hardness = st.sidebar.slider("Hardness", 0.0, 350.0, 120.0)
# solids = st.sidebar.slider("Solids (mg/L)", 0.0, 30000.0, 3000.0)
# chloramines = st.sidebar.slider("Chloramines", 0.0, 15.0, 7.0)
# sulfate = st.sidebar.slider("Sulfate (mg/L)", 0.0, 500.0, 330.0)
# conductivity = st.sidebar.slider("Conductivity (µS/cm)", 0.0, 800.0, 420.0)
# organic_carbon = st.sidebar.slider("Organic Carbon (mg/L)", 0.0, 30.0, 10.0)
# trihalomethanes = st.sidebar.slider("Trihalomethanes", 0.0, 150.0, 65.0)
# turbidity = st.sidebar.slider("Turbidity (NTU)", 0.0, 10.0, 4.0)

# # ---------------- INPUT DATA ----------------
# input_dict = {
#     "ph": ph,
#     "Hardness": hardness,
#     "Solids": solids,
#     "Chloramines": chloramines,
#     "Sulfate": sulfate,
#     "Conductivity": conductivity,
#     "Organic_carbon": organic_carbon,
#     "Trihalomethanes": trihalomethanes,
#     "Turbidity": turbidity
# }

# input_df = pd.DataFrame([input_dict])[features]

# st.subheader("Selected Input Values")
# st.dataframe(input_df)

# # ---------------- PREDICTION ----------------
# if st.button("Predict Water Quality"):
#     scaled_input = scaler.transform(input_df)
#     prediction = model.predict(scaled_input)

#     st.divider()
#     st.subheader("Prediction Result")

#     if prediction[0] == 1:
#         st.success("The water is classified as POTABLE.")
#     else:
#         st.error("The water is classified as NON-POTABLE.")

#     # ---------------- USE CASES ----------------
#     st.divider()
#     st.subheader("Suitable Water Use Cases")

#     usecase_text = assign_usecases(input_df.iloc[0])
#     st.info(usecase_text)

#     # ---------------- TREATMENT ----------------
#     st.divider()
#     st.subheader("Recommended Cleaning / Treatment Process")

#     treatment_text = recommend_treatment(input_df.iloc[0])

#     with st.expander("Why these treatments are recommended", expanded=True):
#         st.write(treatment_text)





# 3rd code







# import streamlit as st
# import pandas as pd
# import joblib
# import numpy as np


# # ---------- PAGE CONFIG ----------
# st.set_page_config(
#     page_title="HYDRO-INFORMATICS SYSTEM",
#     layout="wide"
# )

# # ---------- CUSTOM CSS ----------
# st.markdown(
    
#     # <style>
#     #     @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&display=swap');

#     #     .main-title {
#     #         font-family: 'Poppins', sans-serif;
#     #         font-size: 48px;
#     #         font-weight: 700;
#     #         color: #0A2E5D;
#     #         text-align: center;
#     #         margin-top: 10px;
#     #         margin-bottom: 30px;
#     #     }

#     #     .section-title {
#     #         font-family: 'Poppins', sans-serif;
#     #         font-size: 22px;
#     #         font-weight: 600;
#     #         color: #0A2E5D;
#     #         margin-top: 25px;
#     #         margin-bottom: 10px;
#     #     }

#     #     .card {
#     #         background-color: #111827;
#     #         border: 1px solid #1f2937;
#     #         border-radius: 12px;
#     #         padding: 16px;
#     #         margin-top: 10px;
#     #     }
#     # </style>
    
#     unsafe_allow_html=True
# )

# # ---------- MAIN TITLE ----------
# # st.markdown(
# #     '<div class="main-title">Hydroinformatics System</div>',
# #     unsafe_allow_html=True
# # )


# # --------------------------------------------------
# # PAGE CONFIG
# # --------------------------------------------------
# # st.set_page_config(
# #     page_title="Hydroinformatics System",
# #     layout="wide"
# # )

# # --------------------------------------------------
# # LOAD MODEL ARTIFACTS
# # --------------------------------------------------
# @st.cache_resource
# def load_artifacts():
#     model = joblib.load("water_potability_rf_model.pkl")  # ✅ correct filename
#     scaler = joblib.load("scaler.pkl")
#     features = joblib.load("features.pkl")
#     return model, scaler, features


# try:
#     model, scaler, features = load_artifacts()
# except Exception as e:
#     st.error("Error loading model files. Ensure all .pkl files are present.")
#     st.stop()

# # --------------------------------------------------
# # MAIN TITLE
# # --------------------------------------------------
# st.markdown(
#     """
#     <h1 style='text-align:center; color:#1f4e79; font-weight:800; font-size:48px;'>
#         Hydroinformatics System
#     </h1>
#     <hr>
#     """,
#     unsafe_allow_html=True
# )

# # --------------------------------------------------
# # SIDEBAR INPUTS
# # --------------------------------------------------
# st.sidebar.markdown(
#     "<h3 style='font-weight:800;'>Water Parameters</h3>",
#     unsafe_allow_html=True
# )

# ph = st.sidebar.slider("pH", 0.0, 14.0, 7.0)
# hardness = st.sidebar.slider("Hardness", 0.0, 500.0, 120.0)
# solids = st.sidebar.slider("Solids (mg/L)", 0.0, 50000.0, 3000.0)
# chloramines = st.sidebar.slider("Chloramines", 0.0, 15.0, 7.0)
# sulfate = st.sidebar.slider("Sulfate (mg/L)", 0.0, 500.0, 330.0)
# conductivity = st.sidebar.slider("Conductivity (µS/cm)", 0.0, 1000.0, 420.0)
# organic_carbon = st.sidebar.slider("Organic Carbon (mg/L)", 0.0, 30.0, 10.0)
# trihalomethanes = st.sidebar.slider("Trihalomethanes", 0.0, 120.0, 65.0)
# turbidity = st.sidebar.slider("Turbidity (NTU)", 0.0, 10.0, 4.0)

# # --------------------------------------------------
# # INPUT DATAFRAME
# # --------------------------------------------------
# input_df = pd.DataFrame([{
#     "ph": ph,
#     "Hardness": hardness,
#     "Solids": solids,
#     "Chloramines": chloramines,
#     "Sulfate": sulfate,
#     "Conductivity": conductivity,
#     "Organic_carbon": organic_carbon,
#     "Trihalomethanes": trihalomethanes,
#     "Turbidity": turbidity
# }])

# # --------------------------------------------------
# # SHOW INPUT VALUES
# # --------------------------------------------------
# st.subheader("Selected Input Values")
# st.dataframe(input_df, use_container_width=True)

# # --------------------------------------------------
# # CENTERED PREDICT BUTTON
# # --------------------------------------------------
# col1, col2, col3 = st.columns([1, 2, 1])
# with col2:
#     predict_clicked = st.button("Predict Water Quality", use_container_width=True)

# # --------------------------------------------------
# # RULE-BASED FUNCTIONS
# # --------------------------------------------------
# def assign_usecases(row):
#     if row["Turbidity"] <= 5 and row["Solids"] <= 1000:
#         return "Drinking Water;Public & Municipal Use"
#     elif row["Solids"] <= 5000:
#         return "Agricultural Use;Industrial Cooling;Energy Production"
#     else:
#         return "Not recommended for standard use"

# def recommend_treatment(row):
#     steps = []
#     if row["Solids"] > 1500:
#         steps.append("High solids detected – sedimentation and filtration recommended")
#     if row["Chloramines"] > 4:
#         steps.append("Excess chloramines – dechlorination required")
#     if row["Trihalomethanes"] > 80:
#         steps.append("High THMs – reduce chlorination and remove organic precursors")
#     if row["Turbidity"] > 5:
#         steps.append("High turbidity – coagulation and filtration required")
#     return ";".join(steps) if steps else "Standard treatment is sufficient"

# # --------------------------------------------------
# # PREDICTION
# # --------------------------------------------------
# if predict_clicked:
#     X = input_df[features]
#     X_scaled = scaler.transform(X)
#     prediction = model.predict(X_scaled)[0]

#     st.subheader("Prediction Result")

#     if prediction == 1:
#         st.success("The water is classified as POTABLE.")
#     else:
#         st.error("The water is classified as NON-POTABLE.")

#     # --------------------------------------------------
#     # USE CASES (CARD STYLE)
#     # --------------------------------------------------
#     st.subheader("Suitable Water Use Cases")

#     usecases = assign_usecases(input_df.iloc[0]).split(";")

#     if usecases[0] == "Not recommended for standard use":
#         st.warning("This water is not recommended for standard applications.")
#     else:
#         cols = st.columns(len(usecases))
#         for col, case in zip(cols, usecases):
#             with col:
#                 st.markdown(
#                     f"""
#                     <div style="
#                         padding:15px;
#                         background-color:#0e2a47;
#                         border-radius:10px;
#                         text-align:center;
#                         font-weight:600;
#                         color:white;">
#                         {case.strip()}
#                     </div>
#                     """,
#                     unsafe_allow_html=True
#                 )

#     # --------------------------------------------------
#     # TREATMENT RECOMMENDATIONS (BLOCKS)
#     # --------------------------------------------------
#     st.subheader("Recommended Cleaning / Treatment Process")

#     treatments = recommend_treatment(input_df.iloc[0]).split(";")

#     with st.expander("Why these treatments are recommended", expanded=True):
#         for step in treatments:
#             st.markdown(
#                 f"""
#                 <div style="
#                     margin-bottom:10px;
#                     padding:12px;
#                     border-left:5px solid #1f77b4;
#                     background-color:#111827;
#                     border-radius:6px;">
#                     {step.strip()}
#                 </div>
#                 """,
#                 unsafe_allow_html=True
#             )







# 4th code









# import streamlit as st
# import pandas as pd
# import joblib
# import numpy as np

# # ---------- PAGE CONFIG ----------
# st.set_page_config(
#     page_title="HYDRO-INFORMATICS SYSTEM",
#     layout="wide"
# )

# # ---------- CUSTOM CSS ----------
# st.markdown(
#     """
#     <style>
#         @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600;700&display=swap');

#         .main-title {
#             font-family: 'Poppins', sans-serif;
#             font-size: 48px;
#             font-weight: 700;
#             color: #0A2E5D;
#             text-align: center;
#             margin-top: 10px;
#             margin-bottom: 30px;
#         }

#         .section-title {
#             font-family: 'Poppins', sans-serif;
#             font-size: 22px;
#             font-weight: 600;
#             color: #0A2E5D;
#             margin-top: 25px;
#             margin-bottom: 10px;
#         }

#         .card {
#             background-color: #111827;
#             border: 1px solid #1f2937;
#             border-radius: 12px;
#             padding: 16px;
#             margin-top: 10px;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # ---------- LOAD MODEL ARTIFACTS ----------
# @st.cache_resource
# def load_artifacts():
#     model = joblib.load("water_potability_rf_model.pkl")  # Make sure this file exists
#     scaler = joblib.load("scaler.pkl")
#     features = joblib.load("features.pkl")
#     return model, scaler, features

# try:
#     model, scaler, features = load_artifacts()
# except Exception as e:
#     st.error(f"❌ Error loading model files: {e}")
#     st.stop()

# # ---------- MAIN TITLE ----------
# st.markdown(
#     """
#     <h1 style='text-align:center; color:#1f4e79; font-weight:800; font-size:48px;'>
#         Hydroinformatics System
#     </h1>
#     <hr>
#     """,
#     unsafe_allow_html=True
# )

# # ---------- SIDEBAR INPUTS ----------
# st.sidebar.markdown(
#     "<h3 style='font-weight:800;'>Water Parameters</h3>",
#     unsafe_allow_html=True
# )

# ph = st.sidebar.slider("pH", 0.0, 14.0, 7.0)
# hardness = st.sidebar.slider("Hardness", 0.0, 500.0, 120.0)
# solids = st.sidebar.slider("Solids (mg/L)", 0.0, 50000.0, 3000.0)
# chloramines = st.sidebar.slider("Chloramines", 0.0, 15.0, 7.0)
# sulfate = st.sidebar.slider("Sulfate (mg/L)", 0.0, 500.0, 330.0)
# conductivity = st.sidebar.slider("Conductivity (µS/cm)", 0.0, 1000.0, 420.0)
# organic_carbon = st.sidebar.slider("Organic Carbon (mg/L)", 0.0, 30.0, 10.0)
# trihalomethanes = st.sidebar.slider("Trihalomethanes", 0.0, 120.0, 65.0)
# turbidity = st.sidebar.slider("Turbidity (NTU)", 0.0, 10.0, 4.0)

# # ---------- INPUT DATAFRAME ----------
# input_df = pd.DataFrame([{
#     "ph": ph,
#     "Hardness": hardness,
#     "Solids": solids,
#     "Chloramines": chloramines,
#     "Sulfate": sulfate,
#     "Conductivity": conductivity,
#     "Organic_carbon": organic_carbon,
#     "Trihalomethanes": trihalomethanes,
#     "Turbidity": turbidity
# }])

# # ---------- SHOW INPUT VALUES ----------
# st.subheader("Selected Input Values")
# st.dataframe(input_df, use_container_width=True)

# # ---------- CENTERED PREDICT BUTTON ----------
# col1, col2, col3 = st.columns([1, 2, 1])
# with col2:
#     predict_clicked = st.button("Predict Water Quality", use_container_width=True)

# # ---------- RULE-BASED FUNCTIONS ----------
# def assign_usecases(row):
#     if row["Turbidity"] <= 5 and row["Solids"] <= 1000:
#         return "Drinking Water;Public & Municipal Use"
#     elif row["Solids"] <= 5000:
#         return "Agricultural Use;Industrial Cooling;Energy Production"
#     else:
#         return "Not recommended for standard use"

# def recommend_treatment(row):
#     steps = []
#     if row["Solids"] > 1500:
#         steps.append("High solids detected – sedimentation and filtration recommended")
#     if row["Chloramines"] > 4:
#         steps.append("Excess chloramines – dechlorination required")
#     if row["Trihalomethanes"] > 80:
#         steps.append("High THMs – reduce chlorination and remove organic precursors")
#     if row["Turbidity"] > 5:
#         steps.append("High turbidity – coagulation and filtration required")
#     return ";".join(steps) if steps else "Standard treatment is sufficient"

# # ---------- PREDICTION ----------
# if predict_clicked:
#     try:
#         X = input_df[features]
#         X_scaled = scaler.transform(X)
#         prediction = model.predict(X_scaled)[0]

#         st.subheader("Prediction Result")

#         if prediction == 1:
#             st.success("The water is classified as POTABLE.")
#         else:
#             st.error("The water is classified as NON-POTABLE.")

#         # ---------- USE CASES ----------
#         st.subheader("Suitable Water Use Cases")
#         usecases = assign_usecases(input_df.iloc[0]).split(";")

#         if usecases[0] == "Not recommended for standard use":
#             st.warning("This water is not recommended for standard applications.")
#         else:
#             cols = st.columns(len(usecases))
#             for col, case in zip(cols, usecases):
#                 with col:
#                     st.markdown(
#                         f"""
#                         <div style="
#                             padding:15px;
#                             background-color:#0e2a47;
#                             border-radius:10px;
#                             text-align:center;
#                             font-weight:600;
#                             color:white;">
#                             {case.strip()}
#                         </div>
#                         """,
#                         unsafe_allow_html=True
#                     )

#         # ---------- TREATMENT RECOMMENDATIONS ----------
#         st.subheader("Recommended Cleaning / Treatment Process")
#         treatments = recommend_treatment(input_df.iloc[0]).split(";")

#         with st.expander("Why these treatments are recommended", expanded=True):
#             for step in treatments:
#                 st.markdown(
#                     f"""
#                     <div style="
#                         margin-bottom:10px;
#                         padding:12px;
#                         border-left:5px solid #1f77b4;
#                         background-color:#111827;
#                         border-radius:6px;">
#                         {step.strip()}
#                     </div>
#                     """,
#                     unsafe_allow_html=True
#                 )
#     except Exception as e:
#         st.error(f"❌ Error during prediction: {e}")


import streamlit as st
import pandas as pd
import joblib
import numpy as np

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="HYDRO-INFORMATICS SYSTEM",
    layout="wide"
)

# ---------- MAIN TITLE ----------
st.markdown(
    """
    <h1 style='text-align:center; color:white; font-weight:900; font-size:48px;'>
        HYDRO-INFORMATICS SYSTEM
    </h1>
    <hr>
    """,
    unsafe_allow_html=True
)

# ---------- LOAD MODEL ARTIFACTS ----------
@st.cache_resource
def load_artifacts():
    model = joblib.load("water_potability_rf_model.pkl")
    scaler = joblib.load("scaler.pkl")
    features = joblib.load("features.pkl")
    return model, scaler, features

try:
    model, scaler, features = load_artifacts()
except Exception as e:
    st.error("Error loading model files. Ensure all .pkl files are present.")
    st.stop()

# ---------- SIDEBAR INPUTS ----------
st.sidebar.markdown(
    "<h3 style='font-weight:800;'>Water Parameters</h3>",
    unsafe_allow_html=True
)

ph = st.sidebar.slider("pH", 0.0, 14.0, 7.0)
hardness = st.sidebar.slider("Hardness", 0.0, 500.0, 120.0)
solids = st.sidebar.slider("Solids (mg/L)", 0.0, 50000.0, 3000.0)
chloramines = st.sidebar.slider("Chloramines", 0.0, 15.0, 7.0)
sulfate = st.sidebar.slider("Sulfate (mg/L)", 0.0, 500.0, 330.0)
conductivity = st.sidebar.slider("Conductivity (µS/cm)", 0.0, 1000.0, 420.0)
organic_carbon = st.sidebar.slider("Organic Carbon (mg/L)", 0.0, 30.0, 10.0)
trihalomethanes = st.sidebar.slider("Trihalomethanes", 0.0, 120.0, 65.0)
turbidity = st.sidebar.slider("Turbidity (NTU)", 0.0, 10.0, 4.0)

# ---------- INPUT DATAFRAME ----------
input_df = pd.DataFrame([{
    "ph": ph,
    "Hardness": hardness,
    "Solids": solids,
    "Chloramines": chloramines,
    "Sulfate": sulfate,
    "Conductivity": conductivity,
    "Organic_carbon": organic_carbon,
    "Trihalomethanes": trihalomethanes,
    "Turbidity": turbidity
}])

# ---------- SHOW INPUT VALUES ----------
st.subheader("Selected Input Values")
st.dataframe(input_df, use_container_width=True)

# ---------- CENTERED PREDICT BUTTON ----------
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    predict_clicked = st.button("Predict Water Quality", use_container_width=True)

# ---------- RULE-BASED FUNCTIONS ----------
# def assign_usecases(row):
#     if row["Turbidity"] <= 5 and row["Solids"] <= 1000:
#         return "Drinking Water;Public & Municipal Use"
#     elif row["Solids"] <= 5000:
#         return "Agricultural Use;Industrial Cooling;Energy Production"
#     else:
#         return "Not recommended for standard use"

# def recommend_treatment(row):
#     steps = []
#     if row["Solids"] > 1500:
#         steps.append("High solids detected – sedimentation and filtration recommended")
#     if row["Chloramines"] > 4:
#         steps.append("Excess chloramines – dechlorination required")
#     if row["Trihalomethanes"] > 80:
#         steps.append("High THMs – reduce chlorination and remove organic precursors")
#     if row["Turbidity"] > 5:
#         steps.append("High turbidity – coagulation and filtration required")
#     return ";".join(steps) if steps else "Standard treatment is sufficient"
def assign_usecases(row):
    usecases = []

    if 6.5 <= row['ph'] <= 8.5 and row['Turbidity'] <= 5 and row['Trihalomethanes'] <= 0.1 and row['Sulfate'] <= 400:
        usecases.append("Drinking Water")

    if row['Hardness'] <= 500 and row['Solids'] <= 500:
        usecases.append("Domestic Use (washing, cleaning)")

    if row['Sulfate'] <= 400 and row['Conductivity'] <= 1000:
        usecases.append("Agricultural Use")

    if row['Conductivity'] <= 1500 and row['Turbidity'] <= 10:
        usecases.append("Energy Production (cooling / hydropower)")

    if row['Chloramines'] >= 0.2 and row['Turbidity'] <= 5:
        usecases.append("Public & Municipal Use")

    if row['Organic_carbon'] <= 10 and row['Trihalomethanes'] <= 0.1:
        usecases.append("Medical & Scientific Uses (Strict Quality)")

    return "; ".join(usecases) if usecases else "Not recommended for standard use"


def recommend_treatment(row):
    recommendations = []

    if row['ph'] < 6.5:
        recommendations.append("pH is acidic → Lime / alkaline treatment required")
    elif row['ph'] > 8.5:
        recommendations.append("pH is basic → Acid dosing for correction")

    if row['Hardness'] > 500:
        recommendations.append("High hardness → Ion exchange or lime-soda softening")

    if row['Solids'] > 500:
        recommendations.append("High solids → Sedimentation and filtration")

    if row['Chloramines'] < 0.2:
        recommendations.append("Low disinfectant → Add chlorination")
    elif row['Chloramines'] > 2:
        recommendations.append("Excess chloramines → Dechlorination required")

    if row['Sulfate'] > 400:
        recommendations.append("High sulfate → Reverse Osmosis / Ion Exchange")

    if row['Conductivity'] > 1000:
        recommendations.append("High salinity → Desalination (RO)")

    if row['Organic_carbon'] > 10:
        recommendations.append("High organic carbon → Activated carbon / AOP")

    if row['Trihalomethanes'] > 0.1:
        recommendations.append("High THMs → Reduce chlorination / precursor removal")

    if row['Turbidity'] > 5:
        recommendations.append("High turbidity → Filtration and sedimentation")

    return "; ".join(recommendations) if recommendations else "Water within acceptable limits"


# ---------- PREDICTION ----------
if predict_clicked:
    X = input_df[features]
    X_scaled = scaler.transform(X)
    prediction = model.predict(X_scaled)[0]

    st.subheader("Prediction Result")
    if prediction == 1:
        st.success("The water is classified as POTABLE.")
    else:
        st.error("The water is classified as NON-POTABLE.")

    # ---------- USE CASES ----------
    st.subheader("Suitable Water Use Cases")
    usecases = assign_usecases(input_df.iloc[0]).split(";")

    if usecases[0] == "Not recommended for standard use":
        st.warning("This water is not recommended for standard applications.")
    else:
        cols = st.columns(len(usecases))
        for col, case in zip(cols, usecases):
            with col:
                st.markdown(
                    f"""
                    <div style="
                        padding:15px;
                        background-color:#0e2a47;
                        border-radius:10px;
                        text-align:center;
                        font-weight:600;
                        color:white;">
                        {case.strip()}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    # ---------- TREATMENT RECOMMENDATIONS ----------
    st.subheader("Recommended Cleaning / Treatment Process")
    treatments = recommend_treatment(input_df.iloc[0]).split(";")

    with st.expander("Why these treatments are recommended", expanded=True):
        for step in treatments:
            st.markdown(
                f"""
                <div style="
                    margin-bottom:10px;
                    padding:12px;
                    border-left:5px solid #1f77b4;
                    background-color:#111827;
                    border-radius:6px;">
                    {step.strip()}
                </div>
                """,
                unsafe_allow_html=True
            )
