# Define a function that accepts roll number and returns whether
# the student is present or absent.
import random


def attendance(_input, roll_number):
    if _input in roll_number:
        print('Present')
    else:
        print('Absent')


_list = []
for i in range(11):
    no = random.randint(1, 100)
    _list.append(no)
print(_list)

number = int(input("\nEnter a number \nEnter 'q' to exit: "))
attendance(number, _list)
