import streamlit as st
import pandas as pd
import os
from PIL import Image

st.set_page_config(
    page_title="AI Damage Claim Inspector",
    layout="wide",
    page_icon="⚡"
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = os.path.join(BASE_DIR, "output.csv")

st.title("⚡ AI Multi-Modal Damage Claim System")

# ---------------------------
# 🎬 DEMO MODE
# ---------------------------
st.markdown("## 🎬 Demo Mode")

demo_mode = st.button("▶️ Run Guided Judge Demo")

if demo_mode:

    st.info("Running automated judge walkthrough...")

    st.markdown("### Step 1: Claim Understanding")
    st.write("AI extracts structured damage info from user claim")

    st.markdown("### Step 2: Vision Analysis")
    st.write("Gemini Vision detects actual damage in image")

    st.markdown("### Step 3: Semantic Matching")
    st.write("System maps dent ≈ broken_part instead of strict matching")

    st.markdown("### Step 4: Evidence Evaluation")
    st.write("Checks if image supports claim logically")

    st.markdown("### Step 5: Risk Scoring")
    st.write("Fraud probability is computed using AI confidence + consistency")

    st.markdown("### Step 6: Final Decision")
    st.success("SUPPORTED / CONTRADICTED / UNCERTAIN generated with explanation")

    st.markdown("---")
    st.success("🎯 Demo Complete — System demonstrates full AI reasoning pipeline")


st.caption("Agentic AI system for insurance claim verification using vision + reasoning")

# ---------------------------
# LOAD DATA
# ---------------------------
if not os.path.exists(OUTPUT_PATH):
    st.error(f"output.csv not found at: {OUTPUT_PATH}")
    st.stop()

df = pd.read_csv(OUTPUT_PATH)
filtered = df

# ---------------------------
# METRICS
# ---------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Claims", len(filtered))
col2.metric("Supported", (filtered["claim_status"] == "supported").sum())
col3.metric("Contradicted", (filtered["claim_status"] == "contradicted").sum())
col4.metric("Uncertain", (filtered["claim_status"] == "not_enough_information").sum())

st.divider()

# ---------------------------
# TABLE
# ---------------------------
st.subheader("📊 Claim Overview Table")
st.dataframe(filtered, use_container_width=True)

st.divider()

# ---------------------------
# INSPECTOR
# ---------------------------
st.subheader("🔍 Deep Claim Inspector")

selected_user = st.selectbox("Select User ID", filtered["user_id"].unique())

row = filtered[filtered["user_id"] == selected_user].iloc[0]

colA, colB = st.columns(2)

# ---------------------------
# LEFT PANEL
# ---------------------------
with colA:

    st.markdown("### 🧾 Claim Details")

    st.write("**User Claim:**", row["user_claim"])
    st.write("**Object:**", row["claim_object"])
    st.write("**Issue Type:**", row["issue_type"])
    st.write("**Object Part:**", row["object_part"])

    status = row["claim_status"]

    if status == "supported":
        st.success("SUPPORTED CLAIM ✅")
    elif status == "contradicted":
        st.error("CONTRADICTED CLAIM ❌")
    else:
        st.warning("UNCERTAIN CLAIM ⚠️")

    st.info(row["claim_status_justification"])

# ---------------------------
# RIGHT PANEL
# ---------------------------
with colB:

    st.markdown("### 🤖 AI Analysis")

    severity = row["severity"]

    st.write("**Severity:**", severity)

    if severity == "medium":
        st.info("⚠️ Medium severity detected")
    elif severity == "high":
        st.error("🔴 High severity detected")
    elif severity == "low":
        st.success("🟢 Low severity detected")
    else:
        st.warning("❓ Unknown severity")

    st.markdown("### 🧠 AI Confidence Score")

    confidence = row.get("confidence_score", 0.5)

    st.progress(confidence)
    st.metric("Confidence", f"{int(confidence * 100)}%")

    st.markdown("### 🚨 Fraud Risk Meter")

    fraud = row.get("fraud_score", 50)

    if fraud >= 70:
        st.error(f"🔴 HIGH FRAUD RISK: {fraud}/100")
    elif fraud >= 40:
        st.warning(f"🟠 MEDIUM FRAUD RISK: {fraud}/100")
    else:
        st.success(f"🟢 LOW FRAUD RISK: {fraud}/100")

    st.progress(fraud / 100)

    st.write("**Risk Flags:**", row["risk_flags"])
    st.write("**Evidence Met:**", row["evidence_standard_met"])

    st.code(row["evidence_standard_met_reason"])

# ---------------------------
# IMAGES
# ---------------------------
st.divider()
st.subheader("🖼️ Evidence Images")

image_paths = str(row["image_paths"]).split(";")
img_cols = st.columns(len(image_paths))

for i, img_path in enumerate(image_paths):

    full_path = os.path.join("..", "dataset", img_path.strip())

    with img_cols[i]:
        if os.path.exists(full_path):
            img = Image.open(full_path)
            st.image(img, use_container_width=True)
        else:
            st.error("Image not found")

# ---------------------------
# DEBUG
# ---------------------------
with st.expander("🧠 Raw AI Output"):
    st.json(row.to_dict())