import json
from fastapi import APIRouter, FastAPI, HTTPException


router = APIRouter()
app = FastAPI()


def load_employees():
	with open("../../data/employee.json", "r") as f:
		return json.load(f)


@router.get("/employees1")
def get_employees_json():
	return load_employees()

@router.get("/employees1/{employee_id}")
def get_employee_json_by_id(employee_id: int):
	employees = load_employees()
	for employee in employees:
		if employee["id"] == employee_id:
			return employee
	return {"error": "Employee not found"}


@router.post("/employees1", status_code=201)
def create_employee_json(employee: dict):
	employees = load_employees()
	if any(e["id"] == employee["id"] for e in employees):
		raise HTTPException(status_code=409, detail=f"Employee with id {employee['id']} already exists")
	employees.append(employee)
	with open("../../data/employee.json", "w") as f:
		json.dump(employees, f)
	return {"message": "Employee created successfully", "employee": employee}


@router.delete("/employees1/{employee_id}", status_code=204)
def delete_employee_json(employee_id: int):
	employees = load_employees()
	for employee in employees:
		if employee["id"] == employee_id:
			employees.remove(employee)
			with open("../../data/employee.json", "w") as f:
				json.dump(employees, f)
			return {"message": "Employee deleted successfully"}
	raise HTTPException(status_code=404, detail="Employee not found")






