from fastapi import APIRouter
from app.schemas import LoanApplication
from app.logic import evaluate_loan

router = APIRouter()

@router.post("/decision")
def make_decision(app_data: LoanApplication):
    return evaluate_loan(app_data)
print("🧠 routes.py is being loaded...")