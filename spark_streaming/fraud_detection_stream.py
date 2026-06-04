import csv
from datetime import datetime
from pathlib import Path


INPUT_FILE = Path("data/sample_transactions.csv")
OUTPUT_FILE = Path("output/fraud_scored_transactions_generated.csv")


def apply_fraud_rules(transaction):
    """
    Applies sample fraud rules to one transaction record.

    This is a local runnable simulation of fraud scoring logic.
    In a production streaming pipeline, this same logic can be applied inside
    Spark Streaming or another distributed processing framework.
    """

    amount = float(transaction["amount"])
    country = transaction["country"]
    status = transaction["transaction_status"]

    if amount >= 3000 and country != "US":
        fraud_score = 95
        risk_level = "HIGH"
        rule_triggered = "HIGH_AMOUNT_LOCATION_REVIEW"
    elif amount >= 3000:
        fraud_score = 80
        risk_level = "HIGH"
        rule_triggered = "HIGH_AMOUNT"
    elif status == "failed":
        fraud_score = 60
        risk_level = "MEDIUM"
        rule_triggered = "FAILED_TRANSACTION"
    elif country != "US":
        fraud_score = 45
        risk_level = "MEDIUM"
        rule_triggered = "LOCATION_REVIEW"
    else:
        fraud_score = 10
        risk_level = "LOW"
        rule_triggered = "NONE"

    transaction["fraud_score"] = fraud_score
    transaction["risk_level"] = risk_level
    transaction["rule_triggered"] = rule_triggered
    transaction["processing_timestamp"] = datetime.utcnow().isoformat()

    return transaction


def read_transactions(file_path):
    with open(file_path, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def write_scored_transactions(file_path, transactions):
    file_path.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "transaction_id",
        "customer_id",
        "amount",
        "merchant_category",
        "country",
        "transaction_status",
        "transaction_timestamp",
        "fraud_score",
        "risk_level",
        "rule_triggered",
        "processing_timestamp"
    ]

    with open(file_path, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(transactions)


def main():
    transactions = read_transactions(INPUT_FILE)

    scored_transactions = [
        apply_fraud_rules(transaction)
        for transaction in transactions
    ]

    write_scored_transactions(OUTPUT_FILE, scored_transactions)

    print(f"Processed {len(scored_transactions)} transactions")
    print(f"Generated output file: {OUTPUT_FILE}")

    for transaction in scored_transactions:
        print(
            transaction["transaction_id"],
            transaction["fraud_score"],
            transaction["risk_level"],
            transaction["rule_triggered"]
        )


if __name__ == "__main__":
    main()
