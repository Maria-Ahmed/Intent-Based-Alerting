# Intent-Based-Alerting
The project involves implementing an alert system based on the buying intent of contacts to assist the Business Development team increase their conversion rate. It involves, analyzing transaction data, validating email addresses, and finally sending an alert system to notify the team.

## Repository Structure
Intent-Based-Alerting/
├── data/
│   ├── db_src.duckdb
│   └── db.duckdb
├── notebooks/
│   ├── segmentation.ipynb
│   └── email_validation.ipynb
├── alerts/
│   └── send_alerts.py
├── architecture/
│   └── architecture_diagram.png
├── generate_data.py
├── transactions.csv
├── users.csv
├── requirements.txt
└── README.md

## Table of Contents
- [Overview](#overview)
- [Setup](#setup)
- [Customer Segmentation](#customer-segmentation)
- [Email Validation](#email-validation)
- [Alert System Automation](#alert-system-automation)
- [Architecture Diagram](#architecture-diagram)
- [Objectives](#objectives)

## Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/Maria-Ahmed/Intent-Based-Alerting.git
    cd Intent-Based-Alerting
    ```
2. Generate example data:
    ```bash
    python generate_data.py
    ```
3. Ensure you have the necessary CSV files (`transactions.csv` and `users.csv`) in the repository directory.

## Customer Segmentation
### Objective
Derive a customer segmentation based on high, medium, or low buying intent.

### Instructions
- Copy `data/db_src.duckdb` to `data/db.duckdb`.
- Use the following rules to segment companies based on buying intent:
  - **HIGH**: At least one website visit and at least one news publication within the last 7 days.
  - **MEDIUM**: At least one news publication within the last 30 days.
  - **LOW**: If none of the above applies.
- Complete the segmentation in `notebooks/segmentation.ipynb`.

### Assumptions
- Current date is April 30th, 2024.

## Email Validation
### Objective
Validate email addresses for all companies with high buying intent.

### Instructions
- Use an email verification API to validate email addresses.
- Write the validated email addresses back into the CRM database.
- Complete the email validation in `notebooks/email_validation.ipynb`.

## Alert System Automation
### Objective
Send alert messages to the Business Development team for contacts with high buying intent and a valid email address.

### Instructions
- Use [webhook.site](https://webhook.site/) or another messaging API to send alerts.
- Follow the specified payload structure for the POST request:
  ```json
  {
      "from": "<from-email-address>",
      "to": "biz-dev@taktile.com",
      "message": "<message-goes-here>",
      "subject": "<subject-goes-here>"
  }

