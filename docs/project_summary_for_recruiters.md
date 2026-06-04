# Project Summary for Recruiters

## Project Name

Real-Time Fraud Streaming Pipeline

## Business Problem

Financial organizations need faster visibility into suspicious transaction activity. Batch reporting can delay fraud review, so streaming-style processing helps classify transaction risk sooner and supports fraud monitoring teams.

## What This Project Demonstrates

This project demonstrates a financial transaction data engineering pattern using synthetic transaction data, fraud scoring rules, warehouse-style SQL design, and dashboard metric documentation.

## Tools and Concepts Used

- Python
- Kafka-style ingestion concept
- Spark Streaming-style processing concept
- SQL
- Redshift-style warehouse design
- Fraud rule processing
- Risk classification
- Analytics output design

## Data Flow

Synthetic transaction records are read from a sample CSV file, processed through fraud scoring rules, classified by risk level, and written as scored transaction output for downstream analytics.

## Key Engineering Concepts

- Event-driven data processing pattern
- Rule-based fraud scoring
- Risk classification
- Input and output data validation
- Analytics table design
- Dashboard metric planning
- Clear technical documentation

## Why the Main Script Uses Local Python

The main script is intentionally written in runnable Python so hiring teams can execute and review the logic without needing local Kafka, Spark, Java, or cloud infrastructure setup.

In a production environment, the same fraud scoring logic could be implemented in Spark Streaming, Kafka Streams, Flink, or another distributed stream processing framework.

## Portfolio Safety Note

This project uses synthetic data only. It does not include employer-owned code, production data, customer information, credentials, or confidential architecture.

## Why This Matters

This project shows practical understanding of how financial transaction data can be processed and scored to support fraud detection, analytics, and risk monitoring teams.
