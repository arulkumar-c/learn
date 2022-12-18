from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('arul-topic',
                        group_id='arulGroup', enable_auto_commit=False,
                        bootstrap_servers=['localhost:9092'], api_version=(2, 0, 2),
          				value_deserializer=lambda m: json.loads(m.decode('utf-8')))
for message in consumer:
   print (message.topic)
   print (message.partition)
   print (message.offset)
   print(message.key)