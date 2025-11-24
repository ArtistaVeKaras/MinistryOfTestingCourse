import csv

# Define the file path for the CSV file
file_path = r"c:\Users\Owner\Documents\repos\mot_test_notes\sample_data.csv"

# Sample data to write to the CSV
data = [
    ["ID", "Name", "Age", "Email"],
    [1, "Alice", 30, "alice@example.com"],
    [2, "Bob", 25, "bob@example.com"],
    [3, "Charlie", 35, "charlie@example.com"],
    [4, "Diana", 28, "diana@example.com"]
]

# Write data to the CSV file
with open(file_path, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file created at: {file_path}")