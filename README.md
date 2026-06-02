# AWS Infrastructure Monitor

An automated AWS infrastructure monitoring system with 
CloudWatch dashboards, alarms, SNS alerts, and 
Lambda auto-remediation.

## AWS Services Used
- CloudWatch (dashboards, metrics, alarms)
- SNS (email notifications)
- Lambda (auto-stop idle EC2)
- EC2 (monitored resource)
- S3 (monitored resource)
- EventBridge (hourly Lambda trigger)
- AWS Budgets (cost alerts)
- IAM (least-privilege roles)

## Features
- Live dashboard monitoring EC2, Lambda, S3 metrics
- Automatic email alerts when CPU > 70%
- Auto-stops idle EC2 instances to save cost
- Monthly budget alert at $10 spend
- Lambda error monitoring


## Screenshots
![Dashboard](screenshots/dashboard.png)
![Alarms](screenshots/alarms.png)
![Email Alert](screenshots/email-alert.png)

## Setup Steps
1. Launch EC2 t2.micro instance
2. Create SNS topic and confirm email subscription
3. Create 3 CloudWatch alarms linked to SNS
4. Build CloudWatch dashboard with 5 widgets
5. Deploy auto-stop Lambda with EventBridge hourly trigger
6. Set AWS Budget alert at $0/month
