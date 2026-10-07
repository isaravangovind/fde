import csv

# file_path = "data/homework_invoices.csv"
file_path = "../../data/invoices.csv"


# Method to read a CSV file
def read_csv_file(file_path):
    with open(file_path, mode="r") as file:
        csv_reader = csv.DictReader(file)
        return list(csv_reader)

# Method to Print all rows in the CSV file
def print_all_rows(csv_data):
    print("############ ALL ROWS BEGIN ##############")
    column_names = list(csv_data[0].keys())
    print(column_names[0], column_names[1], column_names[2])
    for row in csv_data:
        print(row)
    print("############ ALL ROWS ENDS ##############")

##### Identify invoices where the amount is greater than 100,000 #####
def identify_high_value_invoices(csv_data):
    high_value_invoices = []
    for row in csv_data:
        try:
            if float(row.get('amount', 0)) > 100000:
                high_value_invoices.append((row.get('invoice_id'), row.get('vendor'), row.get('amount')))
        except ValueError as value_error:
            continue  # Skip rows with invalid amount values
            print(f"Error occurred while processing row: {value_error}")

    for invoice in high_value_invoices:
        value = invoice[0], invoice[1], invoice[2]
        print(value)
    return high_value_invoices

# Missing or invalid amount handling
def handle_missing_or_invalid_amount(csv_data):
    missing_or_invalid_amount = []
    for row in csv_data:
        try:
            amount = float(row.get('amount', 0))
        except ValueError:
            missing_or_invalid_amount.append((row.get('invoice_id'), row.get('vendor'), row.get('amount')))
            print(f"Missing or invalid amount for invoice {row.get('invoice_id')} from vendor {row.get('vendor')}.")
    return missing_or_invalid_amount

# Write matching records into another CSV
def write_high_value_invoices_to_csv(high_value_invoices, output_file_path):
    with open(output_file_path, mode="w", newline='') as file:
        fieldnames = ['invoice_id', 'vendor', 'amount']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for invoice in high_value_invoices:
            writer.writerow({'invoice_id': invoice[0], 'vendor': invoice[1], 'amount': invoice[2]})

# Group totals by vendor
def group_totals_by_vendor(csv_data):
    vendor_totals = {}
    for row in csv_data:
        vendor = row.get('vendor')
        try:
            amount = float(row.get('amount', 0))
        except ValueError:
            continue  # Skip rows with invalid amount values
        vendor_totals[vendor] = vendor_totals.get(vendor, 0) + amount

    for vendor, total in vendor_totals.items():
        print(vendor, total)
    return vendor_totals

print("#### Method to Print all rows in the CSV file ####")
print_all_rows(read_csv_file(file_path))
print("#### Identify invoices where the amount is greater than 100,000 ####")
print(identify_high_value_invoices(read_csv_file(file_path)))
print("#### Missing or invalid amount handling ####")
print(handle_missing_or_invalid_amount(read_csv_file(file_path)))
print("#### Writing high-value invoices to CSV ####")
print(write_high_value_invoices_to_csv(identify_high_value_invoices(read_csv_file(file_path)), "../../data/high_value_invoices.csv"))
print("#### Group totals by vendor ####")
print(group_totals_by_vendor(read_csv_file(file_path)))