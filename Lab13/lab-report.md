# ETL vs ELT Lab — PySpark

A hands-on lab demonstrating the architectural difference between ETL and ELT pipelines using PySpark on a simulated e-commerce orders dataset.

---

## Setup

### Prerequisites
- Python 3.12
- Java 17 (Eclipse Adoptium Temurin recommended)
- `winutils.exe` and `hadoop.dll` in `C:\hadoop\bin` (Windows only)

### Install dependencies
```bash
python -m venv venv
venv\Scripts\activate
pip install pyspark==3.5.5 pyarrow
```

### Run
```bash
python etl_elt_lab.py
```

---

## What the script does

| Part | Description |
|------|-------------|
| Part 1 — ETL | Transforms raw data (normalize casing, fill nulls, filter cancelled) **before** writing clean Parquet to `data/etl_output/orders_clean` |
| Part 2 — ELT | Loads raw data as-is to `data/elt_output/orders_raw`, then transforms via Spark SQL into a clean view and a category summary mart |
| Part 3 | Compares row counts and schemas between both pipeline outputs |

---

## Discussion Questions

### 1. Both pipelines produced the same final output. What is the key architectural difference between them?

The difference is **when** transformation happens relative to loading.

In the **ETL** pipeline, data is cleaned and shaped in memory first, nulls filled, casing normalized, cancelled rows dropped, `order_month` derived, and only the clean result is written to storage. The raw data is never persisted.

In the **ELT** pipeline, the raw data is written to storage first exactly as received, and all transformation logic runs afterward as SQL queries against that stored raw data. The destination system (here, Spark + Parquet) does the transformation work.

---

### 2. The ELT pipeline preserved the raw data in `orders_raw`. Why is this valuable when business requirements change?

Because raw data is the source of truth. Once ETL discards or modifies data during ingestion, that information is gone, you cannot recover the original values without re-extracting from the source.

With ELT, `orders_raw` always contains the unmodified original records. If a business rule changes, for example, if "cancelled" orders need to be included in a new refund analysis, you simply write a new SQL query against the raw table. No re-ingestion, no pipeline rerun, no data loss. This is the foundation of the **data lakehouse** pattern used by tools like Delta Lake and Apache Iceberg.

---

### 3. The ELT pipeline built a `category_summary` mart as a second SQL step without touching the ETL path. How does this demonstrate ELT's flexibility?

The category summary was created by writing a second `spark.sql()` query directly against `orders_raw`, no changes to any existing pipeline code were needed. This shows that ELT treats the raw layer as a reusable foundation: multiple downstream marts, reports, or models can be derived independently from the same raw data at any time.

In an ETL model, building a new output like this would typically require modifying the transformation logic or adding a new pipeline branch before the load step. In ELT, it is just another query.

---

### 4. If this dataset were 100 GB on a distributed Spark cluster, which approach would likely perform better and why?

**ELT would likely perform better** at that scale for several reasons:

- The raw load step is a simple file write with no transformation overhead, so ingestion is fast and parallelizable across the cluster.
- Spark SQL transformations run as distributed query plans optimized by the Catalyst engine and executed across all nodes simultaneously.
- The raw data in Parquet is columnar and compressed, so subsequent SQL queries only scan the columns they need (predicate and projection pushdown).
- Multiple teams can run different transformations concurrently against the same raw Parquet without contention.

ETL at 100 GB would require the transformation to complete entirely before any data lands, creating a bottleneck, especially if the transformation logic is complex or iterative.

---

### 5. Identify one real-world scenario where you would still prefer ETL over ELT.

**Sending data to a third-party SaaS CRM (e.g., Salesforce).**

When the destination system is an external API or a tightly-schemaed relational database that you do not control, you must deliver clean, validated, correctly-typed data. You cannot load raw data first and transform later because the target has no transformation capability, it only accepts records that conform to its schema.

In this scenario ETL is the right choice: validate and shape the data before it ever leaves your environment, ensuring only compliant records are sent and reducing the risk of rejected records, API errors, or corrupted downstream state.
