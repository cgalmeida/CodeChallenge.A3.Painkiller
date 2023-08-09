from fastapi import FastAPI
from app.routes.patient_routes import router as patient_routes
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from aio_pika import connect, IncomingMessage


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

async def on_message(message: IncomingMessage):
    txt = message.body.decode("utf-8")
    print((txt))


async def main(loop):
    connection = await connect("amqp://guest:guest@rabbitmq/", loop = loop)

    channel = await connection.channel()

    queue = await channel.declare_queue("hello")

    await queue.consume(on_message, no_ack = True)


@app.on_event("shutdown")
def shutdown_event():
    loop = asyncio.get_event_loop()
    loop.close()

@app.on_event('startup')
def startup():
    print('STARTED')
    loop = asyncio.get_event_loop()
    loop.create_task(main(loop))
    if(loop.is_running()==False):
        loop.run_forever()


@app.get('health-check')
def health_check():
    return True

app.include_router(patient_routes)