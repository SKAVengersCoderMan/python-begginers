# Calculator 2

choose_op = input("Enter operation(A for Arithmetic and G for geometric): ")

def geo():
	shape = input("Enter shape R for Rectangle\nS for Square\nT for Triangle: ")
	p_or_a = input("Enter P for perimeter and A for Area: ")

	if shape == "R":
		if p_or_a == "P":
			lenght = int(input("Enter lenght of rectangle: "))
			width = int(input("Enter width of rectangle: "))
			P = 2*(lenght+width)
			print("Perimeter is", P)
		elif p_or_a == "A":
			lenght = int(input("Enter lenght of rectangle: "))
			width = int(input("Enter width of rectangle: "))
			A = lenght*width
			print("Area is", A)
	elif shape == "S":
		if p_or_a == "P":
			Side = int(input("Enter Side of Square: "))
			P = 2*Side
			print("Perimeter is", P)
		elif p_or_a == "A":
			Side = int(input("Enter side of square: "))
			A = Side*Side
			print("Area is", A)
	elif shape == "T":
		if p_or_a == "P":
			Side1 = int(input("Enter the first Side of triangle: "))
			Side2 = int(input("Enter the second Side of triangle: "))
			Side3 = int(input("Enter the third Side of triangle: "))
			P = Side1+Side2+Side3
			print("Perimeter is", P)
		elif p_or_a == "A":
			b = int(input("Enter the base of triangle: "))
			h = int(input("Enter the height of triangle: "))
			A = 0.5 * b * h
			print("Area is", A)


def arith():
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


if choose_op == "A":
	arith()
elif choose_op == "G":
	geo()