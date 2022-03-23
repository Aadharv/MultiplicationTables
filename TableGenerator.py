from tokenize import Number


print("This is a program to generate a multiplication table")
number =int(input("Enter the number for the multiplication table "))

for i in range(1,13):
    print(number,"x",i,"=", number *i)