# Define a function that accepts a number and returns
# whether the number is even or odd.
def even_or_odd(num):
    if num % 2 == 0:
        print(f'{num} is an even number')
    else:
        print(f'{num} is an odd number')


x = int(input("Enter a number: "))
even_or_odd(x)
