import streamlit as st
import joblib
import numpy as np
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Credit Decision App", page_icon="💸")
st.title("💳 Mini Credit Decision App")

@st.cache_resource
def load_model():
    return joblib.load("app/model.pkl")

model = load_model()

# Initialize session state
if "results" not in st.session_state:
    st.session_state.results = []

st.markdown("Enter your financial info to see if you'd be approved.")

# Form inputs
income = st.number_input("Annual Income", value=50000)
loan_amount = st.number_input("Loan Amount", value=100000)
credit_score = st.slider("Credit Score", 300, 850, value=700)

# Submit button
if st.button("Submit Application"):
    features = np.array([[income, loan_amount, credit_score]])
    prediction = model.predict(features)[0]
    confidence = model.predict_proba(features)[0][int(prediction)]

    label = "APPROVED" if prediction == 1 else "REJECTED"

    st.success(f"Decision: {label}")
    st.write(f"🗒️ Explanation: Model predicts '{label.lower()}' with confidence: {confidence:.2f}")

    st.metric(label="🤖 Model Confidence", value=f"{confidence:.0%}")
    st.progress(confidence)

    # Store the result
    st.session_state.results.append({
        "Income": income,
        "Loan Amount": loan_amount,
        "Credit Score": credit_score,
        "Decision": label
    })

# Display charts if results exist
if st.session_state.results:
    st.subheader("📊 Decision Trends")
    df = pd.DataFrame(st.session_state.results)

    # Bar chart: Approved vs Rejected
    st.plotly_chart(px.histogram(df, x="Decision", color="Decision", title="Approval Outcomes"))

    # Scatter chart: Credit Score vs Income
    st.plotly_chart(
        px.scatter(
            df,
            x="Credit Score",
            y="Income",
            size="Loan Amount",
            color="Decision",
            title="Credit Score vs Income by Decision"
        )
    )

# Sanity check
if credit_score < 400 or loan_amount > income * 10:
    st.warning("⚠️ This application would likely be rejected in a real-world model.")