# List of employee id, name, salary
# and then print only those names with
# length > 6 and salary < 250000

my_list = [
	{ "empid": 1, "name": "John", "salary": 200000 },
	{ "empid": 2, "name": "Jane", "salary": 300000 },
	{ "empid": 3, "name": "Alice", "salary": 150000 },
	{ "empid": 4, "name": "Bob", "salary": 250000 },
	{ "empid": 5, "name": "Charlie", "salary": 100000 }
]
for emp in my_list:
	if len(emp["name"]) > 6 and emp["salary"] < 250000:
		print(emp["name"])