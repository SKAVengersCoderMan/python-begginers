# Number generator

num = int(input("Enter number to start from: "))
num_r = int(input("Enter times to be repeated: "))

print(num)
for i in range(num_r):
	num += 1
	print(num)