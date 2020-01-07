import pika
import random
import time

connection = pika.BlockingConnection(
 pika.ConnectionParameters(host='localhost')) #here i'am connecting to a brokaer
channel = connection.channel()

channel.queue_declare(queue='bufor',durable=True) #create queue names bufor

while(True):
	message = str(random.randrange(0,5,1))
	channel.basic_publish(
	exchange='',
	routing_key='bufor',
	body=message,
	properties=pika.BasicProperties(
		delivery_mode=2,
	)) # make message persistent, when program will crush, message will be still alive
	print("TEST",message)
	time.sleep(random.randrange(0,5,1))

connection.close()

	

