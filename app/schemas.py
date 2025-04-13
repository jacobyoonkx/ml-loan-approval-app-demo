from pydantic import BaseModel

class LoanApplication(BaseModel):
    income: float
    loan_amount: float
    credit_score: int