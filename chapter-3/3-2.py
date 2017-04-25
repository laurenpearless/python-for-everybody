# Rewrite your pay program using try and except so that your program handles
# non-numeric input gracefully by printing a message and exiting the program.
# The following shows two executions of the program:
# Enter hours: 20
# Enter rate: nine
# Error, please enter numeric input
#
# Enter hours: forty
# Error, please enter numeric input

try:
    hours = int(input('Enter hours: '))
    rate = float(input('Enter rate: '))

    overtime_hours = 0
    overtime_rate = rate * 1.5
    pay = 0

    if hours < 41 :
        pay = hours * rate
    else :
        overtime_hours = hours - 40
        hours = 40
        pay = overtime_hours * overtime_rate + hours * rate
    print(pay)
except:
    print('Error, please enter numeric input')
