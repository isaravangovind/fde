from fastapi import FastAPI
import read_employee
import delete_employees
import get_employees
import post_employees

app = FastAPI(title="My First API")
app.include_router(get_employees.router)
app.include_router(post_employees.router)
app.include_router(delete_employees.router)
app.include_router(read_employee.router)
