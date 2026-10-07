from fastapi import APIRouter, HTTPException
from model import Employee
from data import employees

router = APIRouter()

@router.get("/health")
def health():
	return {"status": "ready"}

# Create a new Employee - Post Call

@router.post("/employees", status_code=201)
def create_employee(employee: Employee):
	if any(e["id"] == employee.id for e in employees):
		raise HTTPException(status_code=409, detail=f"Employee with id {employee.id} already exists")
	employees.append(employee.model_dump())
	return {"message": "Employee created successfully", "employee": employee}


