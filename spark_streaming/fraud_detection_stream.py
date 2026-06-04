from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, current_timestamp


def create_spark_session():
    return (
        SparkSession.builder
        .appName("RealTimeFraudStreamingPipeline")
        .getOrCreate()
    )


def apply_fraud_rules(transactions_df):
    """
    Applies sample fraud rules to transaction data.

    Rules demonstrated:
    1. High transaction amount
    2. Failed transaction status
    3. Non-primary country review
    4. Combined high amount and location risk
    """

    scored_df = (
        transactions_df
        .withColumn(
            "fraud_score",
            when((col("amount") >= 3000) & (col("country") != "US"), 95)
            .when(col("amount") >= 3000, 80)
            .when(col("transaction_status") == "failed", 60)
            .when(col("country") != "US", 45)
            .otherwise(10)
        )
        .withColumn(
            "risk_level",
            when(col("fraud_score") >= 80, "HIGH")
            .when(col("fraud_score") >= 40, "MEDIUM")
            .otherwise("LOW")
        )
        .withColumn(
            "rule_triggered",
            when((col("amount") >= 3000) & (col("country") != "US"), "HIGH_AMOUNT_LOCATION_REVIEW")
            .when(col("amount") >= 3000, "HIGH_AMOUNT")
            .when(col("transaction_status") == "failed", "FAILED_TRANSACTION")
            .when(col("country") != "US", "LOCATION_REVIEW")
            .otherwise("NONE")
        )
        .withColumn("processing_timestamp", current_timestamp())
    )

    return scored_df


def main():
    spark = create_spark_session()

    sample_data = [
        ("TXN100001", "CUST1001", 4500.00, "electronics", "US", "approved"),
        ("TXN100002", "CUST1002", 120.50, "grocery", "US", "approved"),
        ("TXN100003", "CUST1003", 850.00, "travel", "GB", "approved"),
        ("TXN100004", "CUST1004", 75.25, "fuel", "US", "failed"),
        ("TXN100005", "CUST1005", 3200.00, "online", "IN", "approved")
    ]

    columns = [
        "transaction_id",
        "customer_id",
        "amount",
        "merchant_category",
        "country",
        "transaction_status"
    ]

    transactions_df = spark.createDataFrame(sample_data, columns)

    fraud_scored_df = apply_fraud_rules(transactions_df)

    fraud_scored_df.show(truncate=False)


if __name__ == "__main__":
    main()
