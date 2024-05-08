# PyBank Script
import csv

# Set path for file
csvpath = "Resources/budget_data.csv"

# Initialize variables
month_count = 0
total_profit = 0
changes = []
month_changes = []

# Open the CSV file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    csv_header = next(csvreader)

    # Read each row of data
    for row in csvreader:
        # Number of months
        month_count += 1

        # Total profit
        total_profit += int(row[1])

        # Calculate changes
        if month_count == 1:
            last_month_profit = int(row[1])
        else:
            change = int(row[1]) - last_month_profit
            changes.append(change)
            month_changes.append(row[0])
            last_month_profit = int(row[1])

# Calculate average change
avg_change = sum(changes) / len(changes)

# Find greatest increase and decrease in profits
max_change = max(changes)
max_month_idx = changes.index(max_change)
max_month = month_changes[max_month_idx]

min_change = min(changes)
min_month_idx = changes.index(min_change)
min_month = month_changes[min_month_idx]

# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${avg_change:.2f}")
print(f"Greatest Increase in Profits: {max_month} (${max_change})")
print(f"Greatest Decrease in Profits: {min_month} (${min_change})")
