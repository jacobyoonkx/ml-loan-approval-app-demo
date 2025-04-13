import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib

# Simulated training data
data = pd.DataFrame({
    "income": [30000, 50000, 25000, 80000, 100000, 40000, 70000, 30000, 20000, 15000],
    "loan_amount": [100000, 150000, 80000, 200000, 300000, 100000, 120000, 500000, 1000000, 2000000],
    "credit_score": [650, 720, 600, 780, 800, 680, 750, 620, 550, 400],
    "approved": [0, 1, 0, 1, 1, 0, 1, 0, 0, 0]  # More rejections added
})


X = data[["income", "loan_amount", "credit_score"]]
y = data["approved"]

model = LogisticRegression()
model.fit(X, y)

joblib.dump(model, "app/model.pkl")
print("✅ Model trained and saved!")

