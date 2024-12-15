Real-Time Data Pipeline for E-Commerce Analysis
Overview
This project implements a modular and scalable data pipeline for processing, analyzing, and visualizing large-scale e-commerce datasets. The pipeline automates data ingestion using Apache NiFi, processes data using PySpark, stores data in MongoDB, and generates actionable insights through Tableau dashboards.
The pipeline covers multiple analytical dimensions, including high-priority order filtering, item trends, sales channels, regional sales distribution, inventory turnover, order fulfillment times, and profit margin analyses. Results are saved as CSV files for visualization in Tableau.

Features
	•	Automated Data Ingestion:
	◦	Automates the flow of raw data into MongoDB using Apache NiFi.
	•	Distributed Data Processing:
	◦	PySpark performs distributed processing and advanced data transformations.
	◦	Includes multiple analyses such as high-priority orders, sales trends, and profit analysis.
	•	Flexible Data Storage:
	◦	MongoDB stores raw and processed data with schema flexibility.
	•	Comprehensive Data Visualization:
	◦	Tableau dashboards present insights such as:
	▪	Total profit by region and item type.
	▪	Sales distribution across regions.
	▪	Sales channel performance (Online vs. Offline).
	▪	Top-selling items.
	▪	Item-wise profit margins.
	▪	Analysis of high-priority orders.
	•	Modular Architecture:
	◦	Designed for scalability and extensibility for future real-time analytics and machine learning.

Technologies and Tools
	•	Programming Language: Python (with PySpark)
	•	Data Processing: PySpark
	•	Database: MongoDB 
	•	Data Ingestion: Apache NiFi
	•	Visualization: Tableau Public
	•	Version Control: GitHub

Pipeline Workflow
1. Data Ingestion
	•	Tool: Apache NiFi
	•	Process:
	◦	Monitors directories or APIs for incoming data.
	◦	Routes raw data into MongoDB using theGetfileand  PutMongoRecord processors.
2. Data Processing
	•	Tool: PySpark
	•	Scripts:
	◦	processing.py:
	▪	Loads data from MongoDB.
	▪	Performs preprocessing, filtering, and advanced analyses.
	▪	Partitions high-priority orders into 64 smaller files for efficient processing.
	▪	Saves results of analyses as separate CSV files.
	◦	combined.py:
	▪	Merges the partitioned files into a single dataset (output_file.csv).
3. Data Storage
	•	Tool: MongoDB
	•	Process:
	◦	Stores raw data ingested from NiFi.
	◦	Saves processed datasets for quick retrieval and visualization.
4. Data Visualization
	•	Tool: Tableau Public
	•	Process:
	◦	Exports processed data (output_file.csv) into Tableau.
	◦	Creates dashboards showcasing trends, revenue, and sales distribution.

Dataset
Description
The dataset contains e-commerce transaction records, including:
	•	Region: Geographic region of the transaction.
	•	Country: Country where the transaction occurred.
	•	Item Type: Product category (e.g., Office Supplies, Beverages).
	•	Sales Channel: Online or Offline sales.
	•	Order Priority: Priority of the order (e.g., High, Critical).
	•	Units Sold, Unit Price, and Unit Cost: Metrics to calculate revenue, profit, and margins.
Download Link
The dataset used for this project is publicly available and can be downloaded from: https://excelbianalytics.com/wp/downloads-18-sample-csv-files-data-sets-for-testing-sales/
Setup Instructions
	1	Download the dataset from the link above.
	2	Place the file in the data/ folder as dataset.csv.
	3	Ensure the filename matches the script configurations or update the script accordingly.

Data Processing
The processing.py script is the core of the pipeline. It processes raw data from MongoDB, performs multiple transformations and analyses, and saves results as CSV files. Below is a detailed breakdown of its functionalities:
1. Data Loading
	•	Connects to MongoDB and retrieves raw data from the collection salesDB.sales_data.
2. Data Preprocessing
	•	Date Conversion:
	◦	Converts Order Date and Ship Date fields into proper date formats for calculations.
	•	Derived Fields:
	◦	Fulfillment Time:
	▪	Computes the number of days between Order Date and Ship Date.
	◦	Profit Margin:
	▪	Adds a calculated field for profit margin as a percentage: Profit Margin (%)=(Profit/Revenue) × 100 
3. Analytical Tasks
The script performs the following analyses and saves results as CSV files:
	1	High-Priority Orders:
	◦	Filters orders with Order Priority = "H" or "C".
	◦	Partitions these orders into 64 smaller files for efficient processing.
	◦	Output: Partitioned files saved in output/high_priority_orders/.
	2	Item-Wise Trends:
	◦	Groups data by Item Type to calculate:
	▪	Total units sold.
	▪	Total revenue.
	▪	Total profit.
	◦	Output: output/top_selling_items.csv.
	3	Regional Sales:
	◦	Groups data by Region to calculate:
	▪	Total revenue.
	▪	Total profit.
	▪	Total units sold.
	◦	Output: output/sales_per_region.csv.
	4	Sales Channel Analysis:
	◦	Groups data by Sales Channel (Online/Offline) to calculate:
	▪	Total revenue.
	▪	Total units sold.
	◦	Output: output/sales_channel_performance.csv.
	5	Inventory Turnover:
	◦	Summarizes total units sold for each Item Type.
	◦	Output: output/inventory_turnover.csv.
	6	Order Fulfillment Times:
	◦	Computes the average fulfillment time (in days) for orders grouped by Region.
	◦	Output: output/order_fulfillment_time.csv.
	7	Profit Margin Analysis:
	◦	Groups data by Item Type to calculate:
	▪	Average profit margin percentage.
	◦	Output: output/profit_margin_analysis.csv.

Steps to Run the Project
Prerequisites
	1	Install the following tools:
	◦	Python 3.10+
	◦	Java 8 or Java 11
	◦	winutils (windows)
	◦	PySpark
	◦	MongoDB
	◦	Apache NiFi
	◦	Tableau Public
	2	Install required Python libraries: #pip install pyspark pandas

Execution Steps
	1	Download the Dataset:
	◦	Download the dataset from the link-https://excelbianalytics.com/wp/downloads-18-sample-csv-files-data-sets-for-testing-sales/
	◦	Place the dataset in the data/ folder as dataset.csv.
	2	Run Python Scripts:
	◦	processing.py:
	▪	Performs preprocessing, filtering, partitioning, and analyses. #python scripts/processing.py

	◦	combined.py:
	▪	Merges the partitioned files into a single dataset (output_file.csv). #python scripts/combined.py

3		Visualize in Tableau:
	◦	Load the output/output_file.csv file into Tableau Public.
	◦	Use the provided dashboard file or create your own dashboards.


Visualization Example
	refer the Visualization file
Future Enhancements
	1	Real-Time Data Ingestion:
	◦	Use Apache NiFi to connect to live data streams or APIs for real-time updates.
	2	Dynamic Data Processing:
	◦	Add support for multiple datasets from various sources (e.g., inventory logs, customer feedback).
	3	Machine Learning Integration:
	◦	Build predictive models for:
	▪	Demand forecasting
	▪	Customer segmentation
	▪	Churn prediction
	4	Cloud Integration:
	◦	Deploy the pipeline on AWS or Google Cloud Platform for scalability and performance optimization.


