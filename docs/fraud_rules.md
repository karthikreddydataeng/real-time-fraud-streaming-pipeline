# Fraud Detection Rules

This document describes sample fraud detection rules used in the real-time transaction streaming pipeline.

## Rule 1: High Amount Transaction

Transactions greater than or equal to 3000 are flagged for high amount review.

## Rule 2: Failed Transaction

Transactions with failed status are flagged for additional monitoring.

## Rule 3: Location Review

Transactions outside the primary operating country are flagged for location review.

## Rule 4: Merchant Pattern Review

Transactions from high-risk merchant categories can be reviewed for unusual behavior.

## Rule 5: Velocity Pattern

Multiple transactions from the same customer within a short time window may indicate suspicious activity.

## Notes

These rules are simplified for portfolio demonstration. In a production environment, fraud detection may include machine learning models, customer history, device behavior, geolocation, and risk scoring models.
