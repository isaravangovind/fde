from fastapi import FastAPI

app = FastAPI(title="My First API")

@app.get("/health")
def health():
	return {"status": "ready"}

invoices = [
		{"id": 1, "vendor": "Vendor A", "amount": 5000},
		{"id": 2, "vendor": "Vendor B", "amount": 15000},
		{"id": 3, "vendor": "Vendor C", "amount": 25000},
	]

@app.get("/invoices")
def get_invoices():
	
	return invoices

