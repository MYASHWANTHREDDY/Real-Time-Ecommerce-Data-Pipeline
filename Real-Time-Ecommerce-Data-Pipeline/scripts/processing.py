from pyspark.sql import SparkSession
from pyspark.sql.functions import to_date, col, datediff, sum as _sum, avg

mongodb_uri = "mongodb://localhost:27017/salesDB.sales_data"

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("MongoDB to Tableau") \
    .config("spark.mongodb.input.uri", mongodb_uri) \
    .config("spark.mongodb.output.uri", mongodb_uri) \
    .config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.12:3.0.0") \
    .config("spark.driver.memory", "4g") \
    .config("spark.executor.memory", "4g") \
    .config("spark.executor.cores", "2") \
    .getOrCreate()

# Load data from MongoDB
df = spark.read.format("mongo").load()

# Data Preprocessing
df = df.withColumn("Order Date", to_date(df["Order Date"], "M/d/yyyy"))
df = df.withColumn("Ship Date", to_date(df["Ship Date"], "M/d/yyyy"))
df = df.withColumn("Fulfillment Time (days)", datediff(df["Ship Date"], df["Order Date"]))
df = df.withColumn("Profit Margin (%)", (col("Total Profit") / col("Total Revenue")) * 100)
df = df.withColumn("_id", col("_id.oid")) 


# Analyses

# 1. Total Sales per Region
sales_per_region = df.groupBy("Region").agg(_sum("Total Revenue").alias("Total Revenue"))
sales_per_region.write.csv("output/sales_per_region.csv", header=True)

# 2. Top Selling Items
top_items = df.groupBy("Item Type").agg(_sum("Units Sold").alias("Units Sold")).orderBy("Units Sold", ascending=False)
top_items.write.csv("output/top_selling_items.csv", header=True)

# 3. Total Profit by Region and Item
profit_by_region_item = df.groupBy("Region", "Item Type").agg(_sum("Total Profit").alias("Total Profit")).orderBy("Total Profit", ascending=False)
profit_by_region_item.write.csv("output/profit_by_region_item.csv", header=True)

# 4. High-Priority Orders
high_priority_orders = df.filter(df["Order Priority"].isin("H", "C"))
high_priority_orders = high_priority_orders.repartition(64)
high_priority_orders.write.csv("output/high_priority_orders.csv", header=True)

# 5. Inventory Turnover
inventory_turnover = df.groupBy("Item Type").agg(_sum("Units Sold").alias("Units Sold")).orderBy("Units Sold", ascending=False)
inventory_turnover.write.csv("output/inventory_turnover.csv", header=True)

# 6. Order Fulfillment Time
fulfillment_analysis = df.groupBy("Region").agg(avg("Fulfillment Time (days)").alias("Avg Fulfillment Time"))
fulfillment_analysis.write.csv("output/order_fulfillment_time.csv", header=True)

# 7. Profit Margin Analysis
profit_margin_analysis = df.groupBy("Item Type").agg(avg("Profit Margin (%)").alias("Profit Margin (%)")).orderBy("Profit Margin (%)", ascending=False)
profit_margin_analysis.write.csv("output/profit_margin_analysis.csv", header=True)

# 8. Sales Channel Performance
sales_channel_performance = df.groupBy("Sales Channel").agg(_sum("Total Revenue").alias("Total Revenue"))
sales_channel_performance.write.csv("output/sales_channel_performance.csv", header=True)

# Stop Spark Session
spark.stop()

print("Analyses completed and CSV files saved in the 'output' folder.")
