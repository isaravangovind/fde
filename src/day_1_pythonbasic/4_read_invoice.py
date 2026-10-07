import csv
import os

# delete the existing high_value_invoices.csv file if it exists
    
if os.path.exists("data/high_value_invoices.csv"):
     os.remove("data/high_value_invoices.csv")

with open("data/homework_invoices.csv", mode="r") as file:
    csv_reader = csv.DictReader(file)
    print("############ ALL ROWS BEGIN ##############")
    print(csv_reader.fieldnames[0], csv_reader.fieldnames[1], csv_reader.fieldnames[2])
    for row in csv_reader:
        # print(row)
        print(row)
    print("############ ALL ROWS ENDS ##############")

    print("##### Identify invoices where the amount is greater than 100,000 #####")
    print(csv_reader.fieldnames[0], csv_reader.fieldnames[1], csv_reader.fieldnames[2])
    file.seek(0)  # Go back to the beginning.
    next(file)   # Skip the header line.
    print("I am here Before the for block")
    for row in csv_reader:
        try:
            if float(row["amount"]) > 100000:
                print(row["invoice_id"], row["vendor"], row["amount"])
        except ValueError as value_error:
            if row["amount"] == "":
                print(row["vendor"], "has an empty amount field.")
            elif row["amount"] is None:
                print(row["vendor"], "has a None amount field.")
            elif type(row["amount"]) == str:
                print(row["vendor"], "has an is string amount field.")
            # print("Error occurred while processing the amount field:", value_error)

    print("##### End here #####")
    print("Print a simple summary")
    file.seek(0)  # Go back to the beginning.
    next(file) 
    invoicecount = 0
    amountgreaterthan100k = 0
    missingORInvalidamount = 0
    invalidamount = 0
    for row in csv_reader:
        invoicecount += 1
        try:
            if float(row["amount"]) > 100000:
                amountgreaterthan100k += 1
        except ValueError as value_error:
            missingORInvalidamount += 1
            print("Error occurred while processing the amount field:", value_error)
    print("Summary:")
    print("Total invoices:", invoicecount)
    print("Invoices with amount greater than 100,000:", amountgreaterthan100k)
    print("Invoices with missing amount:", missingORInvalidamount)
    print("Invoices with invalid amount:", invalidamount)
