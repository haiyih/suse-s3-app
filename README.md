# suse-s3-app

# SUSE EC2 + S3 Flask Application

## Overview
This project demonstrates deployment of a Python Flask application on an AWS EC2 (SUSE Linux Enterprise Server 16) instance that connects to Amazon S3 using an IAM role.

## Architecture
- EC2 Instance: SUSE Linux Enterprise Server 16 (t3.micro)
- Amazon S3 Bucket: suse-s3-assignment
- IAM Role attached to EC2 with S3 permissions
- Flask application running on port 5000

## How It Works
The Flask app uses boto3 to connect to S3 and lists available S3 buckets.

## Run Instructions
```bash
pip install flask boto3
python3 app.py
