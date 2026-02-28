import csv

input_file = "../data/sample_data.csv"
output_file = "../data/cleaned_data.csv"

valid_rows = []
errors = []

with open(input_file, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        row_errors = []

        # Check for missing name
        if not row['name']:
            row_errors.append("Missing name")

        # Check for missing area
        if not row['area']:
            row_errors.append("Missing area")
        else:
            try:
                area_value = float(row['area'])
                if area_value <= 0:
                    row_errors.append("Invalid area (<=0)")
            except ValueError:
                row_errors.append("Area not numeric")

        if row_errors:
            errors.append((row['id'], row_errors))
        else:
            valid_rows.append(row)

# Write cleaned data
with open(output_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["id", "name", "area"])
    writer.writeheader()
    writer.writerows(valid_rows)

print("Validation Complete")
print(f"Valid Rows: {len(valid_rows)}")
print(f"Error Rows: {len(errors)}")

for error in errors:
    print(f"Row ID {error[0]} Errors: {', '.join(error[1])}")