amount = 50000

if amount < 10000:
    print("This should be approved by Supervisor.")
elif amount > 25000:
    print("This should be approved by Manager.")
elif amount > 50000:
	print("This should be approved by Director.")

kk = 5000
match kk:
	case n if n < 10000:
		print("This should be approved by Supervisor.")
	case n if n > 25000:
		print("This should be approved by Manager.")
	case _:
		print("This should be approved by Director.")