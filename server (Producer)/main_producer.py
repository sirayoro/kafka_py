from kafka import KafkaProducer
from datetime import datetime
import time

# тут инициируется продюсер, отправляющий сообщения
producer = KafkaProducer(bootstrap_servers='localhost:9092')

for i in range(300):
    now = datetime.now()
    formatted_datetime = now.strftime("%H:%M:%S, %d %A, %B %Y")

    producer.send('fsight_topic', value=formatted_datetime.encode('utf-8'))
    
    # спим, чтоб было читабельно
    time.sleep(5)

producer.close()