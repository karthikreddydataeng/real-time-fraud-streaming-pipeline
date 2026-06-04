# Real-Time Fraud Streaming Pipeline

## Overview

This project demonstrates a real-time financial transaction streaming pipeline using Apache Kafka, Spark Streaming, Python, SQL, and cloud data warehouse design patterns.

The pipeline simulates how transaction events can be continuously ingested, processed, enriched, scored for fraud risk, and made available for analytics and monitoring teams.

This is a portfolio project created using synthetic data. It does not contain employer-owned code, production data, credentials, or confidential architecture.

## Business Problem

Financial organizations process large volumes of transaction data every day. Fraud and analytics teams need timely access to transaction patterns so they can detect suspicious activity, monitor risk, and support business reporting.

Traditional batch pipelines may delay fraud visibility. A real-time streaming pipeline helps reduce detection delay by continuously processing transaction events as they arrive.

## Architecture

Synthetic Transaction Events
→ Kafka Producer
→ Kafka Topic
→ Spark Streaming Processor
→ Fraud Rule Engine
→ Curated Transaction Output
→ Cloud Warehouse / Analytics Layer
→ Fraud Monitoring Dashboard

## Tools and Technologies

* Apache Kafka
* Spark Streaming
* Python
* SQL
* Databricks concept
* AWS Redshift concept
* Data Warehousing
* Fraud Rule Processing
* Real-Time Data Engineering

## Key Features

* Generates synthetic financial transaction events
* Publishes transaction events into a Kafka-style topic
* Processes streaming events using Spark Streaming logic
* Applies fraud detection rules based on transaction behavior
* Creates curated fraud analytics output
* Includes SQL schema design for downstream reporting
* Documents pipeline design for hiring team review

## Fraud Detection Rules

The project includes sample fraud rules such as:

* High-value transaction detection
* Multiple transactions within a short time window
* Unusual merchant category activity
* Suspicious country or location pattern
* Repeated failed transaction attempts

## Example Use Cases

* Fraud monitoring
* Real-time transaction analytics
* Risk scoring
* Financial operations reporting
* Downstream analytics for business teams

## Project Outcome

This project demonstrates how real-time streaming pipelines can support fraud analytics teams by improving data availability, reducing manual monitoring effort, and enabling faster risk detection.

## Important Note

This project is a portfolio recreation based on enterprise data engineering patterns. It uses synthetic data and does not include any confidential company information.
