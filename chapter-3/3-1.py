# Rewrite your pay computation to give the employee 1.5 times the hourly rate
# for hours worked above 40 hours
#
# Enter hours: 45
# Enter rate: 10
# Pay: 475

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
