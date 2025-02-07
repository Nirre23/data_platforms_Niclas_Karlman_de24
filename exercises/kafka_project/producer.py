from confluent_kafka import Producer
import json

# Kafka producer instans
producer = Producer({'bootstrap.servers': 'localhost:9092'})

# Funktion för att leverera ett meddelande till Kafka
def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic} [{msg.partition}] at offset {msg.offset}")

# Orders att skicka
orders = [
    {"order_id": 1, "product": "Laptop", "quantity": 2},
    {"order_id": 2, "product": "Phone", "quantity": 1},
    {"order_id": 3, "product": "Tablet", "quantity": 3}
]

# Skicka varje order till Kafka
for order in orders:
    order_json = json.dumps(order)
    producer.produce('orders_topic', value=order_json, callback=delivery_report)

# Vänta tills alla meddelanden är levererade
producer.flush()

