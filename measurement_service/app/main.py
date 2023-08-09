from fastapi import FastAPI
from app.routes.measures_routes import router as measures_routes

app = FastAPI()

@app.get('/health-check')
def health_check():
    return True

app.include_router(measures_routes)