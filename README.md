# Docker Data Pipeline

This project demonstrates a containerized data ingestion pipeline using Docker and PostgreSQL.

Pipeline architecture:

CSV → Python → PostgreSQL

Technologies used:

- Python
- Docker
- Docker Compose
- PostgreSQL
- Pandas
- SQLAlchemy

How to run:

docker compose up --build

This will:

1. Start PostgreSQL container
2. Build the ingestion container
3. Load the CSV dataset into PostgreSQL