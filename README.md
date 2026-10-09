# CampusPulse 2026 starter

Small AWS SAM + Python Lambda + API Gateway + DynamoDB teaching prototype.

## Important
- Inspect and merge this scaffold with your existing project; do not overwrite working files blindly.
- The Lambda execution role must already exist and allow CloudWatch Logs plus `dynamodb:PutItem` and `dynamodb:Scan` on the `CampusPulseEvents` table.
- The role ARN is passed into `template.yaml` so SAM does not need to create a new IAM role. Your deployment identity still needs permission to create/update the API, Lambda function, DynamoDB table, and CloudFormation stack.
- The built-in role/password login is a minimal classroom demonstration, not production authentication. Use Amazon Cognito or another established identity provider for production.
- The `Scan`-based data access is acceptable only for a small demo dataset.

## Local setup
Use Python 3.12 and AWS SAM CLI. From the project root:

```bash
python -m venv .venv
# Windows PowerShell:
.\\.venv\\Scripts\\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
sam validate --lint
sam build
```

## Deployment
1. Confirm AWS CLI credentials and region: `aws sts get-caller-identity` and `aws configure get region`.
2. Ensure an existing Lambda execution role has `AWSLambdaBasicExecutionRole` and a least-privilege policy allowing `dynamodb:PutItem` and `dynamodb:Scan` on the table ARN for `CampusPulseEvents`.
3. Generate strong demo passwords and tokens. Do not commit them.
4. Deploy with `sam deploy --guided`. Supply the existing role ARN and the four secrets as parameters. Do not commit `samconfig.toml`.
5. Copy the `ApiBaseUrl` output from CloudFormation.

## Login
POST `/login` with JSON such as `{"role":"operator","password":"YOUR_OPERATOR_PASSWORD"}`.
The response returns a bearer token. Use `Authorization: Bearer TOKEN` for protected endpoints.
- Operator: GET `/events`, `/stats`, `/alerts`
- Admin: all operator actions plus POST `/events`
- GET `/health` is public

## Example event
```json
{"building":"Library-A","room":"A203","event_type":"occupancy","value":42,"unit":"people"}
```

## Limits and next steps
This prototype demonstrates simulated input, a cloud API, persistent storage, simple analytics, role checks, and logs. It does not implement a production-grade identity provider, a custom VPC, automated backup, or a complete disaster-recovery system. Document the real configuration and limitations in your report.
