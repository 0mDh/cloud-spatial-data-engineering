import csv

def read_data(input_file):
    with open(input_file, mode='r') as file:
        return list(csv.DictReader(file))


def validate_rows(rows):
    valid_rows = []
    errors = []

    for row in rows:
        row_errors = []

        if not row['name']:
            row_errors.append("Missing name")

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

    return valid_rows, errors


def write_cleaned_data(output_file, valid_rows):
    with open(output_file, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name", "area"])
        writer.writeheader()
        writer.writerows(valid_rows)


def main():
    input_file = "../data/sample_data.csv"
    output_file = "../data/cleaned_data.csv"

    rows = read_data(input_file)
    valid_rows, errors = validate_rows(rows)
    write_cleaned_data(output_file, valid_rows)

    print("Validation Complete")
    print(f"Valid Rows: {len(valid_rows)}")
    print(f"Error Rows: {len(errors)}")

    for error in errors:
        print(f"Row ID {error[0]} Errors: {', '.join(error[1])}")


if __name__ == "__main__":
    main()