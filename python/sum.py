first = input("enter first number : ")
second = input("enter second number : ")
sum = first + second
print(sum)

# here first and second number is considered as string so sum added first string to second

# NOW,

first = input("enter first number : ")
second = input("enter second number : ")
sum = int(first) + int(second)
print(sum)

# here, first and second is now converted from string to integer and hence gets added up
