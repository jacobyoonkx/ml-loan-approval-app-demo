from fastapi import FastAPI
from app.routes import router

app = FastAPI()
app.include_router(router)
# Include the router from app/routes.py

@app.get("/")
def read_root():
    return {"message": "Welcome to the Mini Credit Decision API"}