from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when


def create_spark_session():
    return (
        SparkSession.builder
        .appName("RealTimeFraudStreamingPipeline")
        .getOrCreate()
    )


def apply_fraud_rules(transactions_df):
    """
    Applies sample fraud rules to streaming transaction data.
    """

    scored_df = transactions_df.withColumn(
        "fraud_risk_flag",
        when(col("amount") >= 3000, "HIGH_AMOUNT")
        .when(col("transaction_status") == "failed", "FAILED_TRANSACTION")
        .when(col("country") != "US", "LOCATION_REVIEW")
        .otherwise("LOW_RISK")
    )

    return scored_df


def main():
    spark = create_spark_session()

    sample_data = [
        ("TXN100001", "CUST1001", 4500.00, "electronics", "US", "approved"),
        ("TXN100002", "CUST1002", 120.50, "grocery", "US", "approved"),
        ("TXN100003", "CUST1003", 850.00, "travel", "GB", "approved"),
        ("TXN100004", "CUST1004", 75.25, "fuel", "US", "failed")
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
