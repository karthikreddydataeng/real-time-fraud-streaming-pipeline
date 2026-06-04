## How to Run

This project is designed so hiring teams can review both the business architecture and the runnable fraud scoring logic.

### 1. Review the Project Design

Start with these files:

- `architecture/architecture_diagram.md`
- `docs/pipeline_design.md`
- `docs/fraud_rules.md`
- `docs/project_summary_for_recruiters.md`
- `dashboards/fraud_metrics.md`

### 2. Review Sample Input and Output

Input file:

- `data/sample_transactions.csv`

Expected output example:

- `output/fraud_scored_transactions.csv`

Generated output after running the script:

- `output/fraud_scored_transactions_generated.csv`

### 3. Run the Fraud Scoring Script Locally

This project uses built-in Python libraries only.

Run:

```bash
python spark_streaming/fraud_detection_stream.py
```

The script will:

1. Read synthetic transactions from `data/sample_transactions.csv`
2. Apply fraud scoring rules
3. Assign fraud score, risk level, and triggered rule
4. Write generated results to `output/fraud_scored_transactions_generated.csv`

## Sample Fraud Logic

The rules are intentionally simple for portfolio review:

- Transactions greater than or equal to 3000 are flagged as high amount risk.
- Failed transactions are flagged for review.
- Transactions outside the United States are flagged for location review.
- High amount transactions outside the United States receive the highest risk score.

## Design Decisions

- Kafka and Spark Streaming are represented as enterprise architecture concepts.
- The main runnable script uses local Python so the project can be tested without complex setup.
- SQL files show how scored fraud data can be modeled for analytics.
- Dashboard documentation shows the type of metrics fraud teams may monitor.
- All data is synthetic and safe for public portfolio use.
```
