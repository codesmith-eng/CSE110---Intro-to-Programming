# Wind chill calculator
print('••••°°° WIND CHILL CALCULATOR °°° ••••')
print()
print('• Input the degree to want by typing f for farhrenheit and c for celsius')
print()
#i prompted the user to enter the value for temperature
value = float(input('What is the temperature? '))

#the initial value for wind
wind_value= 0

#the conversion from celsius to farhrenheit
celsius_to_farhrenheit = float(9 * value / 5 + 32)

#the input for degree 
degree = input("Fahrenheit or Celsius (F/C)? ")
print()

#formula for converting celsius to farhrenheit and calculating the windchill alltogether
def C_to_F(temperature): #temp the parameter for value
    formula_one = 9 * temperature / 5 + 32
    formula_two = 35.74 + (0.6215 * formula_one) - 35.75 * (wind_value ** 0.16) + (0.4275 * formula_one) * (wind_value ** 0.16)
    return formula_two

#the function for calculating the farhrenheit 
def wind_chill():
    formula_three = 35.74 + (0.6215 * value) - 35.75 * (wind_value ** 0.16) + (0.4275 * value) * (wind_value ** 0.16)
    return formula_three

#using range to loop from 5 to 60 at 5 step at a time
for wind_value in range(5, 61, 5):
    if degree.lower() == 'c':
        result = C_to_F(value)#value is the value for the parameter temperature in the function
        
        print(f'As at temperature {celsius_to_farhrenheit:.1f} F°, and wind speed {wind_value} mph. The wind chill is: {result:.2f} F°')
              
    elif degree.lower() == 'f':
        results = wind_chill()
        print(f'As at temperature {value:.1f} F°, and wind speed {wind_value} mph. The wind chill is: {results:.2f} F°')

