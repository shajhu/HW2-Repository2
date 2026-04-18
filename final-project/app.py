import os
import streamlit as st

st.set_page_config(page_title="Intake-to-Note Assistant", layout="centered")

st.title("Intake-to-Note Assistant")
st.write("Convert intake form responses into a structured pharmacist review note and draft client follow-up.")

input_text = st.text_area("Paste intake form responses here", height=250)

if st.button("Generate Note"):
    if not input_text.strip():
        st.warning("Please enter intake data before generating the note.")
    else:
        st.subheader("Structured Pharmacist Review Note")
        st.info("This is a draft output generated from the intake information." )
        st.write("- Review the client history and identify key concerns.")
        st.write("- Summarize intake details in a clear, structured format.")

        st.subheader("Draft Client-Facing Follow-Up")
        st.write("- Use professional, supportive language.")
        st.write("- Keep recommendations general and avoid diagnostic wording.")

        st.subheader("Flagged Concerns")
        st.write("- If higher-risk indicators are present, mark for human review.")

        st.subheader("Review Status")
        st.success("Standard review recommended, pending pharmacist validation.")

st.write("---")
st.write("*Note: This app is a prototype and does not replace professional review.*")
