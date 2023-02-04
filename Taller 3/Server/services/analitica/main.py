import pika
import os

if __name__ == '__main__':
    
    url = os.environ.get('AMQP_URL', 'amqp://guest:guest@localhost:5672/%2f')
    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()

    channel.queue_declare(queue='Reloj_inteligente')
    channel.queue_bind(exchange='amq.topic', queue='Reloj_inteligente', routing_key='#')

    def callback(ch, method, properties, body):
        mensaje = body.decode('utf-8')
        print(" Mensaje".format(mensaje), flush=True)

    channel.basic_consume(queue='Reloj_inteligente', on_message_callback=callback, auto_ack=True)
    channel.start_consuming()