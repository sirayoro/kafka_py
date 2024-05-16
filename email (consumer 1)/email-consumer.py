from kafka import KafkaConsumer

consumer = KafkaConsumer(
    bootstrap_servers='localhost:9092',
    group_id='main',
    auto_offset_reset='earliest'
)

consumer.subscribe('fsight_topic')  # подписываемся на топик

for message in consumer:
    print(f"email client received: {message.value.decode('utf-8')}")

consumer.close()
