
from aio_pika import connect, IncomingMessage
from app.usecases.measurement import MeasurementUseCases
from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create an engine instance
engine = create_engine("postgresql+psycopg2://postgresql/main?user=admin&password=adminpass")

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class QueueMessageUseCases:
    # async def on_message(self, message: IncomingMessage,  db_session: Session = Depends(get_db_session)):
    async def on_message(self, message: IncomingMessage,  db_session: Session = get_db()):
        txt = message.body.decode("utf-8")
        mc = MeasurementUseCases()
        mc.add_patient_from_queue(txt)


    async def main(self, loop):
        connection = await connect("amqp://guest:guest@rabbitmq/", loop = loop)

        channel = await connection.channel()

        queue = await channel.declare_queue("hello")

        await queue.consume(self.on_message, no_ack = True)