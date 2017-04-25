# Write a program to prompt the user for hours and rate per hour
# to compute gross pay
#
# Enter hours: 35
# Enter Rate: 2.75
# Pay: 96.25

hours_prompt = 'Enter hours: '
rate_prompt = 'Enter rate: '

hours = int(input(hours_prompt))
rate = float(input(rate_prompt))
print(hours * rate)
