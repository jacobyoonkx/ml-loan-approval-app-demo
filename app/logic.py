import joblib
import numpy as np

print("📦 Loading ML model...")
model = joblib.load("app/model.pkl")
print("✅ Model loaded.")

def evaluate_loan(app_data):
    # 🔒 Step 2: Sanity check — rule-based override
    if app_data.credit_score < 500 or app_data.loan_amount > app_data.income * 10:
        return {
            "decision": "reject",
            "explanation": "Application rejected due to clearly poor risk indicators (sanity rule)"
        }

    # 🔮 ML prediction
    features = np.array([[app_data.income, app_data.loan_amount, app_data.credit_score]])
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    if prediction == 1:
        return {
            "decision": "approve",
            "explanation": f"ML model predicts approval (confidence: {probability:.2f})"
        }
    else:
        return {
            "decision": "reject",
            "explanation": f"ML model predicts rejection (confidence: {probability:.2f})"
        }
