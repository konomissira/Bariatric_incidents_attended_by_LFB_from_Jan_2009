# Bariatric Incidents Attended by LFB from Jan 2009 to 2024

## Project Description:

This project analyses data on bariatric incidents attended by the London Fire Brigade (LFB). The goal is to process and load the data into a Snowflake powered data warehouse, enabling insightful analysis of the dataset, resource usage, and incident distributions. The project also explores visualisation options and data science approaches to derive actionable insights.

## Tech Stack:

Data Warehouse: Snowflake

Cloud Storage: AWS S3

Programming Languages: Python, SQL

Tools: Grafana for visualisation

Infrastructure as Code: AWS CloudFormation

## Dataset:

The dataset contains information on bariatric incidents, including:
Calendar Year: Year of the incident.
Type of Incident: Description of the incident type.
Property Type: Property details related to the incident.
Borough Name: Name of the borough where the incident occurred.
Pump Count: Number of pumps used.
Pump Minutes Rounded: Total pump usage time.

The dataset was sourced from the London data store.

## ETL Pipeline:

### Data Collection:

The raw data was collected in Excel format and sampled for testing.

### Data Cleaning:

-   Removed unnecessary fields.

-   Standardised field names and formats.

-   Saved the cleaned data as a CSV file for further processing.

### Data Loading:

Cleaned data was uploaded to an AWS S3 bucket.

The Snowflake COPY INTO command was used to load the data into a Snowflake table.
