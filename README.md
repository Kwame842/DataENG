# ✈️ Airflow Project – Flight Price Analysis (Bangladesh)

This project sets up an end-to-end **Apache Airflow pipeline** using **Docker Compose**, designed to process and analyze **flight price data for Bangladesh**. The pipeline supports:
![Architecture](diagram/Flight_Price_Analysis_Pipeline.png)


- MySQL as a **staging** database
- PostgreSQL as the **analytics** database
- Full data ingestion, validation, transformation, and KPI computation

---

## Project Goals

Build a data pipeline that:

1. Ingests raw CSV data into a MySQL staging table
2. Validates and cleans the data
3. Computes KPIs like average fare, booking counts, and seasonal fare trends
4. Loads results into PostgreSQL for analysis

---

## Technologies

- **Airflow** (orchestration)
- **Docker & Docker Compose**
- **MySQL** (staging)
- **PostgreSQL** (analytics)
- **Python** (data processing)
- **CSV Input**: [Flight Price Dataset – Bangladesh (Kaggle)](https://www.kaggle.com/datasets/mahatiratusher/flight-price-dataset-of-bangladesh)

---

## Project Structure

```
.
├── config/                    # Custom config modules
│   ├── __init__.py
│   └── settings.py
├── dags/                      # Airflow DAGs
│   └── flight_price_pipeline.py
├── diagram/                   # Architecture or pipeline diagram
├── docker/
│   └── mysql/                 # MySQL init scripts
├── data/                      # Source data (CSV) and any output
├── logs/                      # Airflow logs
├── plugins/                   # Custom operators/helpers
├── screenshots/               # UI snapshots
├── Dockerfile                 # Custom Airflow image
├── docker-compose.yml         # Docker Compose services
├── requirements.txt           # Python dependencies
└── README.md
```

---

## Features

- 🗃 **Ingestion** of raw CSV into MySQL
- 🧹 **Validation**: Data type checks, null handling, business rules
- 🔁 **Transformation**: Computes total fare and aggregates
- 📈 **KPI Computation**:
  - Average Fare by Airline
  - Booking Count by Airline
  - Most Popular Routes
  - Seasonal Fare Variations (e.g., Eid, winter)
- 📦 **Data Loading** into PostgreSQL for analytics
- 🔐 **Basic Auth**: Airflow Web UI secured (`admin:admin`)
- ⚙️ Custom `config/` modules for reuse in DAGs

---

## Prerequisites

- Docker & Docker Compose installed locally
- Place the raw CSV file in `data/` as `Flight_Price_Dataset_of_Bangladesh.csv`

---

## Configuration Details

### Dockerfile

Extends `apache/airflow:2.8.1-python3.10` with MySQL/PostgreSQL drivers and config:

```dockerfile
FROM apache/airflow:2.8.1-python3.10

USER root
RUN apt-get update && apt-get install -y     gcc     libpq-dev     default-libmysqlclient-dev  && apt-get clean && rm -rf /var/lib/apt/lists/*

USER airflow
COPY ./dags /opt/airflow/dags
COPY ./plugins /opt/airflow/plugins
COPY ./config /opt/airflow/config

ENV PYTHONPATH="${PYTHONPATH}:/opt/airflow/config:/opt/airflow/plugins"
```

### docker-compose.yml

Defines all services:

- `airflow-webserver`, `airflow-scheduler`
- `postgres` (analytics DB)
- `mysql` (staging DB with `init.sql`)
- Correct `PYTHONPATH` and volume mappings

Update `.env` or YAML as needed:

```yaml
- AIRFLOW__CORE__PYTHONPATH=/opt/airflow/config:/opt/airflow/plugins
```

---

## Getting Started

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-repo/airflow-flight-price.git
   cd airflow-flight-price
   ```

2. **Ensure init files exist**  
   ```bash
   touch config/__init__.py
   ```

3. **Place the flight dataset in `data/`**  
   File name: `Flight_Price_Dataset_of_Bangladesh.csv`

4. **Build and run the containers**  
   ```bash
   docker-compose down --volumes --remove-orphans
   docker-compose build
   docker-compose up
   ```

5. **Access the Airflow Web UI**  
   - URL: [http://localhost:8080](http://localhost:8080)  
   - Username: `admin`  
   - Password: `admin`

---

## KPI Logic & DAG Design

Each DAG task performs one pipeline step:

1. **Ingest CSV → MySQL**: Load and map schema
2. **Validate Data**: Missing/null checks, data types, range checks
3. **Transform & Compute KPIs**:
   - `Total Fare = Base Fare + Tax & Surcharge`
   - Group by airline, route, and season
4. **Load to PostgreSQL**: Push analytics-ready tables

Sample config import in a DAG:

```python
from config.settings import settings
```

Example `settings.py`:

```python
settings = {
    "source_db": "mysql",
    "target_db": "postgres",
    "csv_path": "data/Flight_Price_Dataset_of_Bangladesh.csv"
}
```

---


## 🧹 Cleanup

Stop containers and clear volumes:

```bash
docker-compose down --volumes --remove-orphans
```

---

## Contributing

Have ideas or improvements? Fork and submit a pull request, or open a GitHub issue.

---

## License

MIT License. See `LICENSE` file.
