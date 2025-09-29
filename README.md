# PySpark Streaming to PostgreSQL with Docker

This project demonstrates how to stream CSV files into a PostgreSQL database using **Apache Spark (Structured Streaming)** inside Docker containers. It continuously watches a folder for new CSV files, reads them using PySpark, and appends the data to a table in PostgreSQL.

---

![Architecture](Diagram/Flow%20Diagram.png)

## Project Structure

```
.

├──Diagram /                       # Flow diagram for the project
├── docs /                         # Text documents
├── markdown /                     # markdowns          
├── Dockerfile                    # Docker image for Spark app
├── docker-compose.yml           # Docker Compose file to manage Spark and PostgreSQL containers
├── Spark_Streaming_to_Postgres_New.py  # PySpark script for streaming CSVs to Postgres
├──data_generator.py              # Data generator
└── ecommerce_events/            # Folder where new CSV files are placed
```

---

## Technologies Used

- **Apache Spark** (Structured Streaming)
- **PostgreSQL**
- **Python**
- **Docker** + **Docker Compose**

---

## Prerequisites

Ensure you have the following installed:

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- (Optional) [Git](https://git-scm.com/)

---

## Setup Instructions

Follow these steps to set up and run the project:

---

### 1. Clone or Download the Project

```bash
git clone https://github.com/Kwame842/DataENG/Spark_Streaming.git
cd spark-streaming-postgres-docker
```

Or manually download and extract the ZIP.

---

### 2. Place Your CSV Files

Put your `.csv` files inside the `ecommerce_events/` folder.

Each CSV should have the following columns:

- `event_time`, `event_type`, `product_id`, `category_id`, `category_code`, `brand`, `price`, `user_id`, `user_session`

---

### 3. Build and Run the Docker Containers

```bash
docker-compose build
docker-compose up
```

This will:

- Start a PostgreSQL container (`localhost:5432`)
- Build and run the PySpark app in a container
- Watch the `ecommerce_events/` folder for new CSVs

---

### 4. PostgreSQL Details

Once running, the PostgreSQL database is available at:

- **Host:** `localhost`
- **Port:** `5432`
- **Database:** `ecommerce`
- **User:** `postgres`
- **Password:** `*******`

You can connect using tools like **DBeaver**, **pgAdmin**, or the `psql` CLI.

The data is inserted into a table called `events`.

---

### 5. Confirm the Data

Connect to the database and run:

```sql
SELECT * FROM events;
```

To verify data from your CSVs is successfully loaded.

---

## Workflow

- The script runs in an infinite loop.
- Every 5 seconds, it checks the `ecommerce_events/` folder.
- If a new `.csv` file is found, it reads and loads it into PostgreSQL.
- Files are only processed once.

---

## To Stop the Containers

```bash
docker-compose down
```

This will stop and remove the containers.

---

## Example Use Case

You can simulate a data stream by gradually dropping `.csv` files into the `ecommerce_events/` folder. Spark will process each as it appears.

---

## Cleaning Up

To remove all Docker data (containers, images, volumes):

```bash
docker system prune -a
```

Use with caution.

---

## Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

## License

This project is licensed under the MIT License.
