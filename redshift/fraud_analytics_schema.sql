CREATE TABLE fraud_transaction_events (
    transaction_id VARCHAR(50),
    customer_id VARCHAR(50),
    amount DECIMAL(12,2),
    merchant_category VARCHAR(100),
    country VARCHAR(10),
    transaction_status VARCHAR(50),
    fraud_risk_flag VARCHAR(100),
    transaction_timestamp TIMESTAMP
);

CREATE TABLE fraud_daily_summary (
    transaction_date DATE,
    total_transactions BIGINT,
    high_risk_transactions BIGINT,
    failed_transactions BIGINT,
    total_transaction_amount DECIMAL(18,2)
);
