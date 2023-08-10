from fastapi import FastAPI
from app.routes.patient_routes import router as patient_routes
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from app.usecases.queue_message import QueueMessageUseCases


app = FastAPI(docs_url="/api/v1/patient/docs", openapi_url="/api/v1/patient/docs/openapi.json")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

@app.on_event("shutdown")
def shutdown_event():
    loop = asyncio.get_event_loop()
    if(loop.is_running()==False):
        loop.close()

@app.on_event('startup')
def startup():
    qm = QueueMessageUseCases()
    loop = asyncio.get_event_loop()
    loop.create_task(qm.main(loop))
    if(loop.is_running()==False):
        loop.run_forever()


@app.get('health-check')
def health_check():
    return True

app.include_router(patient_routes)