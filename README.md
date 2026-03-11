# Docker Data Pipeline

## Overview

This project demonstrates a simple containerized data ingestion pipeline built with Docker, Python, and PostgreSQL.  
Retail transaction data is extracted from a CSV file, processed using pandas, and loaded into PostgreSQL for downstream analytics.


## Pipeline Architecture

```
CSV Dataset
     │
     ▼
Python Ingestion Script (pandas)
     │
     ▼
Docker Container
     │
     ▼
PostgreSQL Database
     │
     ▼
SQL Queries / Analytics
```

The ingestion process performs the following steps:

1. Read the CSV dataset using pandas
2. Clean the data (remove null values, duplicates, invalid records)
3. Convert data types where necessary
4. Load the cleaned dataset into PostgreSQL

---

## Technologies Used

* Python
* Docker
* Docker Compose
* PostgreSQL
* Pandas
* SQLAlchemy
* Psycopg2

---

## Project Structure

```
docker-data-pipeline
│
├── Dockerfile
├── docker-compose.yml
├── ingest_data.py
├── requirements.txt
├── OnlineRetail.csv
├── data_cleaning.ipynb
└── README.md
```

---

## How to Run the Pipeline

Clone the repository:

```
git clone https://github.com/Kenantkurt/docker-data-pipeline.git
cd docker-data-pipeline
```

Start the pipeline:

```
docker compose up --build
```

This will:

1. Start a PostgreSQL container
2. Build the ingestion container
3. Run the ingestion script
4. Load the dataset into PostgreSQL

---

## Example SQL Query

After the pipeline runs, you can query the data inside PostgreSQL:

```sql
SELECT country, SUM(quantity)
FROM online_retail
GROUP BY country
ORDER BY SUM(quantity) DESC;
```

---

## Purpose of the Project

This project was built as a **data engineering practice project** to demonstrate how to build a simple containerized ingestion pipeline using Docker and PostgreSQL.

---

## Future Improvements

• Add Airflow orchestration  
• Implement incremental data ingestion  
• Add data validation checks  
• Deploy the pipeline to a cloud environment (GCP or AWS)
