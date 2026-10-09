# CampusPulse 2026
## Cloud-Native Smart Campus Operations Platform

**Module:** Big Data & Cloud Computing  
**Cloud provider:** Amazon Web Services (AWS)  
**Region:** Paris (`eu-west-3`)  
**Team:** Joswikkha Dilli Babu, Preethi Krishnamoorthi, Anbuselvan Ponnusamy

---

# Slide 1 — Introduction
- Smart campuses generate readings such as occupancy, energy consumption and temperature.
- CampusPulse demonstrates how these readings can be collected and monitored using cloud services.
- The prototype processes simulated campus events through a REST API.

**Speaker notes:** Introduce the problem and explain that this is a working cloud prototype.

---

# Slide 2 — Objectives
- Receive simulated campus readings.
- Validate and process incoming events.
- Store event records in a cloud database.
- Calculate operational statistics.
- Identify abnormal readings through alerts.
- Observe application execution using cloud logs.

**Speaker notes:** Explain that the project demonstrates the main components of a small cloud-native monitoring platform.

---

# Slide 3 — Architecture
- Amazon API Gateway receives HTTP requests.
- AWS Lambda handles validation, event processing and aggregation.
- Amazon DynamoDB stores campus events.
- AWS IAM provides permissions for AWS resource access.
- Amazon CloudWatch collects Lambda execution logs.
- AWS SAM and CloudFormation support deployment.

**Visual:** Insert the CampusPulse architecture diagram.

**Speaker notes:** Walk through the request path: API Gateway → Lambda → DynamoDB. Explain that CloudWatch collects execution logs and IAM controls permissions.

---

# Slide 4 — Implementation
- Implemented using Python and AWS Lambda.
- Exposed REST endpoints for health checks, login, event submission, retrieval, statistics and alerts.
- Stored events in the `CampusPulseEvents` DynamoDB table.
- Used a Python script to generate simulated campus events.
- Deployed in AWS region `eu-west-3`.

**Speaker notes:** Mention that the application is deployed and was tested against the live API.

---

# Slide 5 — Security
- Demo login distinguishes operator and admin roles.
- Protected endpoints require bearer-token authentication.
- IAM permissions control Lambda access to AWS services.
- CloudWatch logs support troubleshooting.
- The demo authentication is not intended for production use.

**Speaker notes:** Acknowledge the prototype's security limitations and explain what would be needed for production.

---

# Slide 6 — Testing and Results
- Six automated unit tests passed.
- Simulated event submissions returned successful responses.
- Event retrieval was verified.
- Statistics endpoint returned event counts and aggregate values.
- Alerts endpoint returned abnormal occupancy and temperature readings.
- CloudWatch Lambda logs were inspected.

**Speaker notes:** Show the saved evidence screenshots for unit tests, events, statistics, alerts and CloudWatch.

---

# Slide 7 — Cost and Scalability
- Serverless compute avoids managing continuously running application servers.
- DynamoDB on-demand capacity suits a small demonstration workload.
- An AWS budget alert was configured.
- Actual costs must be checked in AWS Billing.
- Higher traffic would require additional load testing and performance evaluation.

**Speaker notes:** Explain the cost-conscious choices without claiming the application is free or production-ready.

---

# Slide 8 — Limitations and Future Work
- Demo authentication rather than a production identity provider.
- No custom VPC or automated backups.
- No complete disaster-recovery implementation.
- Future work could include a dashboard, stronger identity management, automated backups and more extensive monitoring.

**Speaker notes:** Clearly distinguish implemented functionality from future improvements.

---

# Slide 9 — Conclusion and Demo
- CampusPulse demonstrates a deployed serverless campus-event pipeline.
- The application receives, stores and retrieves simulated events.
- Statistics and abnormal readings can be queried through the API.
- Automated tests and CloudWatch logs provide validation evidence.

**Live demo plan:**
1. Call `/health`.
2. Show event records.
3. Show `/stats`.
4. Show `/alerts`.
5. Briefly show unit tests and CloudWatch logs.

**Closing:** CampusPulse demonstrates how AWS serverless services can be combined to build a small, observable and cost-conscious cloud application.