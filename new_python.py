a=int(input("enter a number")
b=int(input("enter a second number")

print(a=b)
print(a-b)
print(a*b)
try:
	value = a/b
except ZeroDivisionError:
	print("Not viable option")
else:
	print("the division answer is:", value)
finally:
	pass
