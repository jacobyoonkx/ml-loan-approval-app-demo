# 💳 Credit Decision Engine (ML + FastAPI + Streamlit)

A lightweight, explainable loan approval engine inspired by decisioning platforms like **Taktile**. This project uses a logistic regression model served with **FastAPI**, and visualized through a **Streamlit** frontend for interactive predictions, confidence scores, and trend analysis.

---
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)]((https://taktile-interview.streamlit.app/))

## 🚀 What It Does

- Predicts loan approval likelihood based on:
  - Annual income
  - Requested loan amount
  - Credit score
- Displays a **model confidence score** per decision
- Includes **rule-based sanity checks** to reject clearly risky applications
- Visualizes approval trends with charts
- Allows users to test multiple scenarios and **track decision history**

---

## ⚙️ Tech Stack

| Layer       | Tool          |
|-------------|---------------|
| ML Model    | scikit-learn  |
| API         | FastAPI       |
| Frontend    | Streamlit     |
| Charts      | Plotly        |
| Dev Setup   | Python + venv |

---

## 📸 Demo Preview

- Streamlit form to enter applicant data
- Real-time decision with confidence bar
- Bar and scatter plots of approval trends

*(Add screenshots here once available)*

---

## 📁 File Structure

```
.
├── app/
│   ├── logic.py              # ML logic and prediction handler
│   ├── schemas.py            # Pydantic data validation models
│   ├── routes.py             # FastAPI route for loan decisioning
│   ├── train_model.py        # Model training script
│   ├── model.pkl             # Saved ML model
│   └── streamlit_app.py      # Frontend UI using Streamlit
├── main.py                   # FastAPI app entry point
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
```

---

## 🧪 How to Run Locally

```bash
git clone https://github.com/your-username/ml-loan-approval-app.git
cd ml-loan-approval-app

python -m venv venv
source venv/bin/activate          # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Train the ML model
python app/train_model.py

# Run FastAPI backend
uvicorn main:app --reload

# In a separate terminal, run Streamlit frontend
streamlit run app/streamlit_app.py
```

---
## 💡 Features

- Rule-based override: Rejects if credit score < 500 or loan > 10x income  
- Confidence display: Shows how certain the model is about each prediction  
- Charts: Visualize decision trends over time  
- Session history: Live results stored and visualized in each user session  

## 📌 Future Ideas

- Add SHAP explainability for model transparency  
- Deploy on Streamlit Cloud / Hugging Face / Render  
- Use real-world dataset for training  
- Add version tracking for the model  

## 🙋‍♂️ Author

Built by [@jacobyoonkx](https://github.com/jacobyoonkx)  
Inspired by real-world credit decisioning platforms like Taktile.
