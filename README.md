# Docker Data Pipeline

## Overview

This project demonstrates a **containerized data ingestion pipeline** built with Python, Docker, and PostgreSQL.

The pipeline reads an e-commerce transaction dataset (CSV), performs basic data cleaning, and loads the processed data into a PostgreSQL database for further analysis.

This project showcases core **data engineering concepts** such as:

* Data ingestion
* Containerization
* Service orchestration
* Database loading
* Basic data quality checks

---

## Pipeline Architecture

```
CSV Dataset
     ↓
Python Ingestion Script
     ↓
Docker Container
     ↓
PostgreSQL Database
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
