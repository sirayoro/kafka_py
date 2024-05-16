from kafka import KafkaConsumer

consumer = KafkaConsumer(
    bootstrap_servers='localhost:9092',
    group_id='main',
    auto_offset_reset='latest'
)

consumer.subscribe('test_topic')  # подписываемся на топик косньюмером (ЕСЛИ ЗАДАНО ИМЯ ТОПИКА, ТО ОН ОБЯЗАТЕЛЬНО ДОЛЖЕН СУЩЕСТВОВАТЬ!!!!)

for message in consumer:
    print(f"sms client received: {message.value.decode('utf-8')}")

consumer.close()
