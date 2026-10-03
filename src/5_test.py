import csv

with open("data/homework_invoices.csv", mode="r") as file:
	csv_reader = csv.DictReader(file)

	vendor_totals = {}
	for row in csv_reader:
		vendor = row["vendor"]
		try:
			amount = float(row["amount"])
		except (ValueError, TypeError):
			continue  # Skip missing or invalid amounts

		vendor_totals[vendor] = vendor_totals.get(vendor, 0) + amount

	for vendor, total in vendor_totals.items():
		print(vendor, total)