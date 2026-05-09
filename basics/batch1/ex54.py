import csv
from pathlib import Path


filename = Path("/home/devops", "counter_table.csv")
with open(filename, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(table_data)