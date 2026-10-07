from fastapi import APIRouter, FastAPI
from data import employees

router = APIRouter()

@router.get("/employees")
def get_employees():
	return employees

@router.get("/employees/{employee_id}")
def get_employee(employee_id: int):
	for employee in employees:
		if employee["id"] == employee_id:
			return employee
	return {"error": "Employee not found"}

@router.get("/employees/name/{name}")
def get_employee_by_name(name: str):
	for employee in employees:
		if employee["name"].lower() == name.lower():
			return employee
	return {"error": "Employee not found"}

