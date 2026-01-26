## AWS Deployment Readiness

This project supports two deployment modes:

### Local Deployment
- Database: SQLite
- Entry file: backend/app.py
- Purpose: Development & testing

### AWS Deployment
- Database: DynamoDB
- Notifications: AWS SNS
- Entry file: backend/aws_app.py
- Services:
  - DynamoDB (CryptoPriceAlerts, AdminAuditLogs)
  - SNS (crypto-alerts topic)

AWS credentials and infrastructure will be configured during deployment.
