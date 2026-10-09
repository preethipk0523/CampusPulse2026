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

Check the health endpoint:

```powershell
Invoke-RestMethod -Method Get -Uri "$ApiUrl/health"
```

To test the remaining endpoints, authenticate using the demo credentials configured during deployment and send the returned token as a bearer token. Do not publish passwords or tokens in the report or source repository.

The Python event generator is located at `scripts/generate_events.py`. It requires the `CAMPUSPULSE_URL` and `CAMPUSPULSE_ADMIN_TOKEN` environment variables.

## 6. Validation Results

The project was tested using automated unit tests and requests to the deployed API.

- Six unit tests passed.
- Simulated campus events were accepted and stored.
- Event retrieval was verified.
- Operational statistics were retrieved.
- Abnormal readings were returned by the alerts endpoint.
- Lambda execution logs were inspected in CloudWatch.

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

