from fastapi import FastAPI, APIRouter, HTTPException
from data import employees

router = APIRouter()

@router.delete("/employees/{employee_id}", status_code=204)
def delete_employee(employee_id: int):
	for employee in employees:
		if employee["id"] == employee_id:
			employees.remove(employee)
			return {"message": "Employee deleted successfully"}
	raise HTTPException(status_code=404, detail="Employee not found")

