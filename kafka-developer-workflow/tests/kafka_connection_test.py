from kafka.admin import KafkaAdminClient

admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:29093",
    request_timeout_ms=5000,
)

try:
    topics = admin_client.list_topics()
    print("Successfully connected to Kafka!")
    print("Available topics:", topics)
finally:
    admin_client.close()
