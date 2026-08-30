

# 📊 YouTube Trending Data Engineering Project (ETL vs. ELT)

**Python** | **SQL / PostgreSQL (Neon)** | **SQLite** | **Power BI** | **Status: Completed**

---

## 📌 Project Overview

A comprehensive Data Engineering project that designs, implements, and compares two primary data pipeline architectures—**ETL (Extract, Transform, Load)** and **ELT (Extract, Load, Transform)**—using YouTube Trending Video datasets. The objective is to evaluate both approaches in terms of execution speed, scalability, resource efficiency, and data transformation capabilities, while delivering actionable insights through interactive BI dashboards.

---

## 🏛️ Team & Academic Institution

* **University:** Princess Nourah Bint Abdulrahman University


* **College:** College of Computer and Information Sciences - Information Systems Department


* **Section / Group:** Group 2 (Section: 63s)


* **Team Members:**
* Jood Ahmed Bagazi


* Mashael Mohammed Algazlan


* Reem Turki Alotaibi


* Shoug Alghaihab


* Nourah Almuharb





---

## 🎯 Problem Statement & Objectives

### ⚠️ The Challenge

YouTube generates vast daily data (views, likes, comments, engagement). Traditional processing methods often lead to slow execution, high resource consumption, and reduced scalability. Choosing the correct pipeline architecture (ETL vs. ELT) is critical for handling large-scale continuous data efficiently.

### 🎯 Key Objectives

1. **Multi-Source Ingestion:** Collect raw data from structured CSVs, JSON metadata, and live YouTube Data APIs.


2. **ETL Implementation:** Extract, clean, transform, and map data in Python before loading into an SQLite database (`youtube_etl.db`).


3. **ELT Implementation:** Extract raw data and load directly into a cloud database warehouse (**Neon PostgreSQL** staging tables), executing SQL-based transformations inside the database.


4. **Automation:** Schedule end-to-end pipeline execution using Windows Task Scheduler.


5. **Performance Comparison:** Benchmark ETL vs. ELT based on execution speed, efficiency, and scalability.


6. **Analytics & Visualization:** Build interactive Power BI dashboards to analyze top categories, engagement rates, and channel trends.



---

## 📂 Data Sources & Processing Methods

* **USvideos.csv:** Primary dataset containing trending video metrics (views, likes, comments).


* **US_category_id.json / legacy_categories:** ID-to-category mapping for readable labels (e.g., Music, Entertainment, Gaming).


* **YouTube Data API v3:** Real-time metadata extraction for live category trending content.



---

## 🔄 ETL vs. ELT Pipeline Architectures

### 1️⃣ ETL Workflow

* **Extract:** Ingested CSV, JSON, and API data using Python (`pandas`, `json`, `requests`).


* **Transform (Python):** Cleaned null values (`dropna`), dropped duplicates (`drop_duplicates`), converted datetimes, mapped categories, and created feature engineering metrics (`engagement_rate = likes / views`).


* **Load:** Saved transformed data into SQLite database (`youtube_etl.db`) and exported `final_data.csv`.



### 2️⃣ ELT Workflow

* **Extract:** Python ingested raw CSV and SQLite category sources.


* **Load First:** Directly pushed raw datasets into **Neon PostgreSQL** cloud staging tables (`stage_usvideos`, `stage_categories`) using `SQLAlchemy`.


* **Transform (SQL in PostgreSQL):** Applied in-database SQL transformations (`COALESCE`, `LEFT JOIN`, numeric casting) to create calculated metrics and output the structured `final_youtube_data` table.


* **Automation:** Automated daily pipeline runs using **Windows Task Scheduler**.



---

## ⚡ Benchmark Comparison (ETL vs. ELT Results)

| Metric | ETL Approach | ELT Approach |
| --- | --- | --- |
| **Execution Speed**<br> | **~6.0 Seconds**<br> | **~0.5 Seconds** (12x Faster)

 |
| **Scalability**<br> | Less Scalable (Limited by external/local memory)

 | Highly Scalable (Leverages cloud database engine)

 |
| **Pipeline Efficiency**<br> | Lower (More data movement before storage)

 | Higher (In-database processing, fewer steps)

 |

---

## 🖥️ Business Intelligence Dashboard (Power BI Highlights)

* **Key Metrics:** Summarized **11M Total Views**, **484K Total Likes**, and **62K Total Comments** across top trending sets.


* **Top Category:** **Music** & **Entertainment** leading total views and interaction counts.


* **Visualizations:** Categorical view distributions, engagement scatter plots, likes distribution donut charts, and channel-level performance leaderboards.
