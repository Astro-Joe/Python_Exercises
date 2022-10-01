# Define a function that accepts 2 values and return its sum,
# subtraction and multiplication.

def operations(value, value1):
    add = value + value1
    print("Sum is = " + str(add))
    sub = value - value1
    print("Sub is = " + str(sub))
    mult = value * value1
    print("Multiplication is = " + str(mult))


a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
operations(a, b)
