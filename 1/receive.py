import pika
import random
import time

connection = pika.BlockingConnection(\
	pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='bufor',durable=True) #checking than queue bufor is exist

print('waiting for message')

def callback(ch, method, properties, body):
	print("Task number: %r" %body)
	
	ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='bufor', on_message_callback=callback)

channel.start_consuming()
