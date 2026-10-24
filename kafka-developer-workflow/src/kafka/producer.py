from kafka import KafkaProducer

class EventProducer:
    def __init__(self, bootstrap_servers="localhost:29093"):
        self.producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

    def publish(self, topic, event):
        future = self.producer.send(topic, value=event.encode('utf-8'))
        return future.get(timeout=10)

    def close(self):
        self.producer.close()
