import streamlit as st
from langflow_graph import run_graph
from translate import translate_to
from voice import speak

st.set_page_config(page_title="MediLens", layout="centered")
st.title("💊 MediLens - AI-Powered Medicine Explainer")

medicine = st.text_input("Enter medicine name")
language = st.selectbox("Select language", ["English", "Hindi", "Gujarati"])

if st.button("Explain"):
    if medicine:
        result = run_graph(medicine, language)
        st.markdown(f"### 🧪 Medicine Information: {result}")
        speak(result, language)
    else:
        st.warning("Please enter a medicine name.")