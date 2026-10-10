# CampusPulse 2026 — Deployment Guide

## 1. Project Overview

CampusPulse 2026 is a serverless smart-campus monitoring prototype deployed on Amazon Web Services (AWS) in the Paris region (`eu-west-3`).

## 2. AWS Architecture

The application uses:

- **Amazon API Gateway** — provides the REST API.
- **AWS Lambda** — validates and processes campus events.
- **Amazon DynamoDB** — stores events in the `CampusPulseEvents` table.
- **AWS IAM** — manages the Lambda execution permissions.
- **Amazon CloudWatch** — collects Lambda execution logs.
- **AWS SAM and CloudFormation** — package and deploy the application.

## 3. Deployed API

**Region:** `eu-west-3`

**API base URL:**  
https://pl5c4u5e85.execute-api.eu-west-3.amazonaws.com/prod

## 4. Available Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health` | Check application health |
| POST | `/login` | Authenticate a demo user |
| POST | `/events` | Submit a campus event (admin) |
| GET | `/events` | Retrieve recorded events |
| GET | `/stats` | Retrieve operational statistics |
| GET | `/alerts` | Retrieve abnormal readings |

Protected endpoints require a valid bearer token in the `Authorization` header. The `/health` endpoint is public.

## 5. Testing the Deployment

Open PowerShell in the project directory and set the API URL:

```powershell
$ApiUrl = "https://pl5c4u5e85.execute-api.eu-west-3.amazonaws.com/prod"
```

### 5.1 Public Health Check
```powershell
Invoke-RestMethod -Method Get -Uri "$ApiUrl/health"
```
*Expected response:* `{"status": "ok", "service": "CampusPulse 2026"}`

### 5.2 Demo Authentication & Protected Endpoints
Authenticate using the demo credentials configured during deployment. Pass `role` (`"operator"` or `"admin"`) and `password` in JSON format:

```powershell
# Authenticate (example shown for operator role)
$LoginPayload = @{
    role = "operator"
    password = "YOUR_OPERATOR_PASSWORD"
} | ConvertTo-Json

$AuthResponse = Invoke-RestMethod -Method Post -Uri "$ApiUrl/login" -ContentType "application/json" -Body $LoginPayload
$Token = $AuthResponse.token
$Headers = @{ Authorization = "Bearer $Token" }

# Retrieve events, operational statistics, and abnormal alerts
Invoke-RestMethod -Method Get -Uri "$ApiUrl/events" -Headers $Headers
Invoke-RestMethod -Method Get -Uri "$ApiUrl/stats" -Headers $Headers | ConvertTo-Json -Depth 5
Invoke-RestMethod -Method Get -Uri "$ApiUrl/alerts" -Headers $Headers | ConvertTo-Json -Depth 5
```

> **Troubleshooting "Invalid credentials":**
> 1. Ensure the JSON key is `"role"` (not `"username"`).
> 2. Ensure the role value is strictly lowercase: `"operator"` or `"admin"`.
> 3. Verify `-ContentType "application/json"` is included so PowerShell does not post form-encoded body text.
> 4. Ensure you provide the configured `OperatorPassword` (demo password), not the `OperatorToken`.
> 5. Do not publish passwords or tokens in reports, slides, or version control.

### 5.3 Simulated Event Ingestion
The Python event generator is located at `scripts/generate_events.py`. It requires the `CAMPUSPULSE_URL` and `CAMPUSPULSE_ADMIN_TOKEN` environment variables:

```powershell
$env:CAMPUSPULSE_URL = $ApiUrl
$env:CAMPUSPULSE_ADMIN_TOKEN = "YOUR_ADMIN_TOKEN"
python scripts/generate_events.py
```

## 6. Validation Results

The project was tested using automated unit tests and requests to the deployed live API:

- **Automated Unit Tests**: All six unit tests passed (`test_validation.py`) verifying schema validation, negative value rejection, threshold triggers, and room aggregation.
- **Simulated Ingestion**: Ingested four simulated events (occupancy, energy, temperature), all returning HTTP `201 Created`.
- **Database Persistence**: Five total records verified in `CampusPulseEvents` (1 pre-existing baseline + 4 newly submitted).
- **Statistics Aggregation**: `/stats` verified returning 5 total events, 1 energy reading (18.5 kWh), 3 alerts, and 180 total latest occupancy across distinct spaces (95 in Library-A A203 + 85 in Building A Room 101).
- **Abnormal Alerts**: `/alerts` verified returning the 3 abnormal readings exceeding defined thresholds.
- **CloudWatch Observability**: Lambda execution logs inspected in CloudWatch log group `/aws/lambda/campuspulse-2026-CampusPulseFunction-...`.

## 7. Security

The prototype uses role-based demo authentication and IAM permissions for AWS resource access. Demo credentials are intended for classroom testing only. A production deployment would require a production-grade identity provider and stronger secret management.

## 8. Monitoring

Lambda execution logs are available in Amazon CloudWatch. These logs can be used to inspect invocations and troubleshoot runtime issues.

## 9. Cost Control

The application uses serverless compute and on-demand DynamoDB capacity to avoid provisioning continuously running servers. An AWS budget alert was configured for cost awareness. Actual charges should be verified in AWS Billing before submission.

## 10. Limitations

The current prototype does not include a custom VPC, automated backups, a complete disaster-recovery system, or a production-grade identity provider. It uses a small demonstration dataset and is not intended for production workloads.

## 11. Cleanup

After the demonstration and after saving all required evidence, unused AWS resources can be removed to avoid future charges.

Before deleting the CloudFormation stack, verify that the project is no longer needed and that all evidence has been saved. The deployed stack is named `campuspulse-2026` in `eu-west-3`.

