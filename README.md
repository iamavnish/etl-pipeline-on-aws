# ETL Pipeline on AWS

## Overview

This is Proof of Concept for ETL (Extract Transform Load) pipeline on AWS.

## Architecture

![etl-pipeline-on-aws](https://github.com/iamavnish/etl-pipeline/assets/13760927/e99657fb-01bc-4062-8543-fa7b6eaa5c94)

## Tech Stack

- AWS
  - EC2
  - S3
  - IAM
- Apache Airflow (hosted on EC2)
- Python3

## Data Set

CSV file containing twitter data - https://github.com/iamavnish/etl-pipeline/blob/main/tweets.csv

## Solution

A file transfer job pushes CSV files (one at a time) containing tweets to a location from where it is being extracted by an ETL job which further does some row level transformations and loads the file into S3. For the ETL process to be successful, the file transfer job must complete successfully before the ETL job starts. Apache Airflow hosted on EC2 is being used for workflow orchestration.

