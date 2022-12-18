from kafka import KafkaProducer
from kafka.errors import KafkaError
import json

# create a producer. broker is running on localhost
producer = KafkaProducer(retries=5, 
						value_serializer=lambda v: json.dumps(v).encode('utf-8'),
						bootstrap_servers=['localhost:9092'], #group_id='arulGroup', 
						api_version=(2, 0, 2))

# define the on success function 
def on_success(record):
   print(record.topic)
   print(record.partition)
   print(record.offset)

# define the on error callback function
def on_error(excp):
   log.error(excp)
   raise Exception(excp)

# send the message to arul-topic
producer.send('arul-topic', {'name': 'arul kumar c'}).add_callback(on_success).add_errback(on_error)

# block until all async messages are sent
producer.flush()