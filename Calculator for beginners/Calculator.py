# Calculator 1

# First number
first_num = int(input("Enter first number: "))
# Second number
second_num = int(input("Enter second number: "))
# Operations
op = input("Enter operation: ")

if op == "+":
	ans = first_num + second_num
elif op == "-":
	ans = first_num - second_num
elif op == "*":
	ans = first_num * second_num
elif op == "/":
	ans = first_num / second_num
else:
	print("invalid")

print("So,", first_num,"and", second_num, "is", ans)