# SageMaker Fraud Model Design

## Purpose

This document explains how an AWS SageMaker model could be integrated into the fraud streaming pipeline for transaction risk scoring.

## Business Problem

Rule-based fraud detection is useful, but it may miss complex fraud patterns. Machine learning can help identify risk based on transaction history, amount behavior, merchant category, country, failed attempts, and customer activity patterns.

## ML Integration Flow

Transaction Events  
→ Feature Preparation  
→ SageMaker Fraud Model Endpoint  
→ Risk Score  
→ Fraud Rule Engine  
→ Analytics Output  
→ Fraud Monitoring Dashboard

## Example Features

- Transaction amount
- Merchant category
- Country
- Transaction status
- Customer transaction frequency
- Failed transaction count
- Average transaction amount
- Time since previous transaction
- High value transaction flag

## Example Model Output

- Fraud probability
- Risk score
- Risk level
- Recommended review flag

## How This Fits the Pipeline

The current portfolio project uses rule-based fraud scoring for local execution. In a production-style design, the same transaction records can be enriched with ML scoring from a SageMaker endpoint before being written to the analytics layer.

## Monitoring Considerations

- Model prediction latency
- Fraud score distribution
- False positive review rate
- Data drift
- Feature freshness
- Model version
- Endpoint availability

## Portfolio Safety Note

This document is a design example only. It does not include production ML code, customer data, trained models, credentials, or confidential fraud logic.
