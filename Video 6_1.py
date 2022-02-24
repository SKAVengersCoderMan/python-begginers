# Chitter Chatter app!

user = input("Hello! I am the computer! You are...\n")
print("Hi " + user)
hobby = input("What do you like to do? I like to live like a computer :)\n")
print("Wow!")
age = float(input("So, what is your age? I am infinite years old ;)\n"))
print("ok..")
ask = input("Do you want to close? Y for yes and N for no.\n")
if ask == "Y":
	print("Good bye")
	pass
elif ask == "N":
	print("Ok.. But I am feeling tired... Shutting Down...")
else:
	print("Error- The answer is not usable...")