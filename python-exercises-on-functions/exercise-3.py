# Define a function in python that accepts 3 values and
# returns the maximum of three numbers.

def max_number(num, num1, num2):
    if num > num1 and num > num2:
        print(f"\n{num} is maximum among all")
    elif num1 > num and num1 > num2:
        print(f"\n{num1} is maximum among all")
    else:
        print(f"\n{num2} is maximum among all")


a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

max_number(a, b, c)
