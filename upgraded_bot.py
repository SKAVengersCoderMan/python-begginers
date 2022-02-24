import datetime
import random

def wish():
	hour = int(datetime.datetime.now().hour)
	if int(hour) < int(12):
		print("Good morning sir")
	if int(hour) >= int(12) and int(hour) < int(16):
		print("Good afternoon sir")
	elif int(hour) >= int(16):
		print("Good evening sir")

def ask():
	input_ = input("What do you want me to do... I can do many things. Try adding with typing a\n")
	if input_ == 'a':
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

if __name__ == '__main__':
	wish()
	while True:
		ask()

