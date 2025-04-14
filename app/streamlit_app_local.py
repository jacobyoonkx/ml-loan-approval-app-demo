import streamlit as st
import requests
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Credit Decision App", page_icon="💸")
st.title("💳 Mini Credit Decision App")

# Initialize session state for storing results
if "results" not in st.session_state:
    st.session_state.results = []

st.markdown("Enter your financial info to see if you'd be approved.")

# Form inputs
income = st.number_input("Annual Income", value=50000)
loan_amount = st.number_input("Loan Amount", value=100000)
credit_score = st.slider("Credit Score", 300, 850, value=700)

# Submit button
# Submit button
if st.button("Submit Application"):
    payload = {
        "income": income,
        "loan_amount": loan_amount,
        "credit_score": credit_score
    }

    # ⚠️ Show warning only on extreme inputs
    if credit_score < 400 or loan_amount > income * 10:
        st.warning("⚠️ This application would likely be rejected in a real-world model.")

    try:
        response = requests.post("http://127.0.0.1:8000/decision", json=payload)

        if response.status_code == 200:
            result = response.json()
            st.success(f"Decision: {result['decision'].upper()}")
            st.write(f"📝 Explanation: {result['explanation']}")

            # 🔍 Parse confidence from explanation
            confidence = None
            if "confidence:" in result["explanation"]:
                try:
                    confidence = float(result["explanation"].split("confidence:")[-1].strip(" )"))
                except ValueError:
                    confidence = None

            # 📈 Show confidence as metric + bar
            if confidence is not None:
                st.metric(label="🤖 Model Confidence", value=f"{confidence:.0%}")
                st.progress(confidence)

            # Store the result
            st.session_state.results.append({
                "Income": income,
                "Loan Amount": loan_amount,
                "Credit Score": credit_score,
                "Decision": result["decision"]
            })
        else:
            st.error("Something went wrong with the API call.")

    except Exception as e:
        st.error(f"Error connecting to API: {e}")


# Display chart if results exist
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