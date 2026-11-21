# Retail Sales Dashboard

import csv
import matplotlib.pyplot as plt

dates = []
sales = []

with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        dates.append(row["Date"] + "-" + row["Product"])
        sales.append(int(row["Sales"]))

print("Sales Data:")
for i in range(len(dates)):
    print(dates[i], ":", sales[i])

# Line Graph
plt.figure(figsize=(8, 5))
plt.plot(dates, sales, marker="o")
plt.title("Retail Sales Analysis")
plt.xlabel("Date and Product")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(dates, sales)
plt.title("Product Sales")
plt.xlabel("Date and Product")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
