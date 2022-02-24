# This is my app!!!

user = input("What is your name?\n")
print("Hello " + user)
age = float(input("Enter your age\n"))
print("I am also", age)

yes_no = input("Do you want to continue? Y for yes and N for no...\n")

if yes_no == "Y":
	print("Ok... Malfunction.. shutting down")
elif yes_no == "N":
	print("Bye!")
else:
	print("Wrong answer")