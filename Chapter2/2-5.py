# Write a program which prompts the user for a Celcius temperature,
# converts the temperature to Fahrenheit, and prints out the converted
# temperature

temp_prompt = 'Enter a temperature in degrees Celcius: '
temp = float(input(temp_prompt))
print(temp*9/5+32)
