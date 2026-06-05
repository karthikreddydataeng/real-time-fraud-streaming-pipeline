# Real-Time Fraud Streaming Pipeline

## Overview

This project demonstrates a real time financial transaction fraud monitoring pipeline using synthetic banking transaction data.

The project shows how transaction records can be ingested, scored using fraud rules, classified by risk level, and prepared for downstream analytics and dashboard reporting.

This is a portfolio project using synthetic data only. It does not contain employer-owned code, production data, customer information, credentials, or confidential architecture.

## Business Problem

Financial organizations process large volumes of customer transactions every day. Fraud and risk teams need faster visibility into suspicious activity so they can identify high-risk transactions, failed attempts, unusual locations, and large-value transactions.

Batch reporting can delay fraud review. A streaming-style pipeline helps process transaction events sooner and makes scored fraud data available for analytics and monitoring.

## Architecture

Synthetic Banking Transactions  
→ Kafka Producer Concept  
→ Kafka Topic Concept  
→ Fraud Scoring Logic  
→ Scored Transaction Output  
→ Redshift Analytics Tables  
→ Fraud Monitoring Dashboard  
→ Optional SageMaker ML Risk Scoring Design

## Tools and Technologies

- Python for local fraud scoring logic
- Apache Kafka concept for real-time transaction ingestion
- Spark Streaming concept for scalable stream processing
- AWS SageMaker concept for ML-based fraud risk scoring
- SQL for fraud analytics table design
- AWS Redshift concept for warehouse reporting
- CSV files for sample input and output data
- Markdown documentation for architecture, fraud rules, and dashboard metrics

## Repository Structure

```text
real-time-fraud-streaming-pipeline/
├── README.md
├── requirements.txt
├── architecture/
│   └── architecture_diagram.md
├── dashboards/
│   └── fraud_metrics.md
├── data/
│   └── sample_transactions.csv
├── docs/
│   ├── fraud_rules.md
│   ├── pipeline_design.md
│   └── project_summary_for_recruiters.md
├── kafka/
│   └── transaction_producer.py
├── ml/
│   └── sagemaker_fraud_model_design.md
├── output/
│   ├── fraud_scored_transactions.csv
│   └── fraud_scored_transactions_generated.csv
├── redshift/
│   └── fraud_analytics_schema.sql
└── spark_streaming/
    └── fraud_detection_stream.py
```

## How to Run

This project demonstrates the business architecture, synthetic transaction data flow, fraud scoring logic, and analytics-ready output for a real-time fraud monitoring pipeline.

### 1. Review the Project Design

Start with these files:

- `architecture/architecture_diagram.md`
- `docs/pipeline_design.md`
- `docs/fraud_rules.md`
- `docs/project_summary_for_recruiters.md`
- `dashboards/fraud_metrics.md`
- `ml/sagemaker_fraud_model_design.md`

### 2. Review Sample Input and Output

Input file:

- `data/sample_transactions.csv`

Expected output example:

- `output/fraud_scored_transactions.csv`

Generated output after running the script:

- `output/fraud_scored_transactions_generated.csv`

### 3. Run the Fraud Scoring Script Locally

This project uses built-in Python libraries only.

From the main project folder, run:

```bash
python spark_streaming/fraud_detection_stream.py
```

If your system uses Python 3 command separately, run:

```bash
python3 spark_streaming/fraud_detection_stream.py
```

The script will:

1. Read synthetic banking transactions from `data/sample_transactions.csv`
2. Apply fraud scoring rules
3. Assign fraud score, risk level, and triggered rule
4. Write generated results to `output/fraud_scored_transactions_generated.csv`
5. Print a transaction-level scoring summary in the terminal

## Sample Fraud Logic

The fraud scoring rules are intentionally simple for portfolio review:

- Transactions greater than or equal to 3000 are flagged as high amount risk.
- Failed transactions are flagged for review.
- Transactions outside the United States are flagged for location review.
- High amount transactions outside the United States receive the highest risk score.

## Sample Output

Example terminal output:

```text
Processed 8 transactions
Generated output file: output/fraud_scored_transactions_generated.csv
TXN100001 80 HIGH HIGH_AMOUNT
TXN100002 10 LOW NONE
TXN100003 45 MEDIUM LOCATION_REVIEW
TXN100004 60 MEDIUM FAILED_TRANSACTION
TXN100005 95 HIGH HIGH_AMOUNT_LOCATION_REVIEW
TXN100006 10 LOW NONE
TXN100007 95 HIGH HIGH_AMOUNT_LOCATION_REVIEW
TXN100008 60 MEDIUM FAILED_TRANSACTION
```

## Design Decisions

- Kafka and Spark Streaming are represented as enterprise architecture concepts.
- The main runnable script uses local Python so the project can be tested without complex setup.
- SageMaker is documented as an optional ML risk scoring extension.
- SQL files show how scored fraud data can be modeled for analytics.
- Dashboard documentation shows the type of metrics fraud teams may monitor.
- All data is synthetic and safe for public portfolio use.

## Key Features

- Synthetic banking transaction input data
- Runnable fraud scoring script
- Expected and generated output files
- Fraud risk classification
- Redshift-style analytics schema
- Dashboard metrics documentation
- SageMaker ML model integration design
- Recruiter-friendly project summary
- Architecture documentation

## Portfolio Safety Note

This project is a portfolio recreation based on financial data engineering patterns. It uses synthetic data and does not include employer-owned code, production data, customer information, credentials, or confidential fraud logic.
