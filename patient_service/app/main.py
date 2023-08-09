import pika
from fastapi import FastAPI, Body
from app.routes.patient_routes import router as patient_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

@app.get('health-check')
def health_check():
    return True

app.include_router(patient_routes)