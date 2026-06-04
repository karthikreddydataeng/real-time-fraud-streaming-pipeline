import json
import random
import time
from datetime import datetime


MERCHANT_CATEGORIES = ["grocery", "travel", "electronics", "fuel", "entertainment", "online"]
COUNTRIES = ["US", "CA", "MX", "IN", "GB", "DE"]


def generate_transaction_event():
    return {
        "transaction_id": f"TXN{random.randint(100000, 999999)}",
        "customer_id": f"CUST{random.randint(1000, 9999)}",
        "amount": round(random.uniform(5, 5000), 2),
        "merchant_category": random.choice(MERCHANT_CATEGORIES),
        "country": random.choice(COUNTRIES),
        "transaction_status": random.choice(["approved", "approved", "approved", "failed"]),
        "transaction_timestamp": datetime.utcnow().isoformat()
    }


def publish_transaction_events():
    """
    Portfolio simulation of a Kafka transaction producer.
    In a real implementation, this function would publish events to a Kafka topic.
    """
    for _ in range(10):
        event = generate_transaction_event()
        print(json.dumps(event))
        time.sleep(1)


if __name__ == "__main__":
    publish_transaction_events()
