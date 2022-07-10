from kafka import KafkaProducer

bootstrap_servers = ['localhost:9091', 'localhost:9092', 'localhost:9093']
topicName = 'my-topic-three'

producer = KafkaProducer(bootstrap_servers = bootstrap_servers)

producer.send(topicName, b'Hello World!')
for i in range(15):
    t_str = f"Hello : {i}"
    producer.send(topicName, t_str.encode('utf'))
producer.flush()
