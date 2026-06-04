# Pipeline Design

## Objective

The objective of this project is to demonstrate how real-time transaction data can be ingested, processed, scored, and prepared for analytics.

## Pipeline Flow

1. Transaction events are generated using a synthetic Python producer.
2. Events are conceptually published into a Kafka topic.
3. Spark Streaming processes incoming transaction events.
4. Fraud rules are applied to classify transactions.
5. Curated transaction records are stored for analytics.
6. Business teams can use downstream dashboards to monitor transaction risk.

## Data Engineering Concepts Demonstrated

- Real-time ingestion
- Streaming data processing
- Event-driven architecture
- Fraud rule processing
- Cloud warehouse schema design
- Analytics-ready data modeling

## Hiring Team Review

This project is designed to show practical understanding of enterprise data engineering patterns including Kafka, Spark Streaming, SQL modeling, and fraud analytics workflows.
