# Output Files for Real-Time Data Pipeline

## Overview
The output files generated by the Real-Time Data Pipeline are essential deliverables that summarize the results of various data processing and analytical steps performed in the project. Due to the large size of these files (over 1 GB), they are stored on Google Drive for easy access.

---

## Accessing the Output Files
You can download all the output files from the following Google Drive link:  
**[Download Output Files](https://drive.google.com/drive/folders/1DGr2hjAa6Di14n3bDu4g37MTLwd6bOK_)**

---

## Output Files Description
Below is a description of the files you will find in the Google Drive link:

### 1. High-Priority Orders
- **Folder**: `high_priority_orders/`
- **Description**:
  - Contains 64 partitioned files with transaction-level details of high-priority orders (`Order Priority = "H" or "C"`).
  - These files are used for parallel processing and downstream merging into `output_file.csv`.

### 2. Summary and Analysis Files
- **`sales_per_region.csv`**:
  - Summary of total revenue, profit, and units sold grouped by region.
- **`top_selling_items.csv`**:
  - Details of the top-selling items, including total units sold, revenue, and profit.
- **`profit_by_region_item.csv`**:
  - Breakdown of profit grouped by region and item type.
- **`inventory_turnover.csv`**:
  - Total units sold for each item type, representing inventory movement.
- **`order_fulfillment_time.csv`**:
  - Average fulfillment time (in days) grouped by region.
- **`profit_margin_analysis.csv`**:
  - Summary of average profit margins (as a percentage) for each item type.
- **`sales_channel_performance.csv`**:
  - Revenue and units sold grouped by sales channel (Online vs. Offline).

### 3. Consolidated Output
- **`output_file.csv`**:
  - A merged dataset created by the `combined.py` script.
  - Contains transaction-level details of high-priority orders.

---

## How to Use These Files

### Tableau Dashboards:
- Use the files, especially `output_file.csv`, to create interactive dashboards showcasing key insights like sales trends, regional performance, and item profitability.

### Further Analysis:
- Use the summary files (`sales_per_region.csv`, `top_selling_items.csv`, etc.) for additional analysis or to build detailed reports.

### Partitioned Data:
- Use the `high_priority_orders/` folder for distributed processing or scaling the pipeline.

---

## Notes
- Ensure you download the files in their respective formats (CSV) for compatibility with tools like Tableau or Python.
- If you encounter any issues accessing the files, please contact the project owner.
