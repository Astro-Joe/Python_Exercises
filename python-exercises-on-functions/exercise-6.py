def factorial(number):
    """ Define a function that returns Factorial of a number."""
    fact = 1
    while number != 0:
        fact *= number
        number = number - 1
    print('Factorial is', fact)
    

num = int(input("Enter a number: "))
factorial(num)