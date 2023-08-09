
import pika
from fastapi import Body

class QueueMessageUseCases:
    async def send_message(self, message: str):
        connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
        channel = connection.channel()
        channel.queue_declare(queue='hello')
        channel.basic_publish(exchange='', routing_key='hello', body=message)
        connection.close()
        return {"status": "message sent"}