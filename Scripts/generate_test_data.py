import csv
import random

# Define the file path for the CSV file
file_path = r"c:\Users\Owner\Documents\repos\mot_test_notes\Excel\test_data.csv"

# Parameters
serviceID = "BTEL1232342343"
product_offering = "YTEL-100"

# Generate 100 records of test data
data = [["RecordID", "ServiceID", "ProductOffering", "CustomerName", "Age", "Email"]]
for i in range(1, 101):
    customer_name = f"Customer{i}"
    age = random.randint(18, 65)
    email = f"customer{i}@example.com"
    data.append([i, serviceID, product_offering, customer_name, age, email])

# Write data to the CSV file
with open(file_path, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"Test data CSV file created at: {file_path}")