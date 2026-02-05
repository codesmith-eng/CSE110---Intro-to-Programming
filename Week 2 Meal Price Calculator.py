#This is a meal price calculator program
print('  ~~~~ MEAL PRICE CALCULATOR ~~~~ ')
#i used \n to create blank space in this program
# I prompt the user to enter the values 
print('\n')

print('Good day customer, I am your meal price calculator in this restaurant, dont worry about calculating your expenses, just input the price, your tax rate and the number of people present and i will do the calculations for you')
print('\n')

price_meal_child=float(input('Please enter the price of a child meal: $'))

# I added to the child meal
child_drink=float(input('Please enter the price of a child drink: $'))
price_meal_adult=float(input('Please enter the price of an adult meal: $'))

# I added to the drink of adults
adult_drink=float(input('Please enter the price of an adult drink: $'))
number_children=int(input('How many children are present: '))
number_adult=float(input('How many adult are present: '))
tax=float(input('What is your Tax rate: $'))

# I calculate the amount for the meal here
child_meal_subtotal=(price_meal_child + child_drink) * number_children
adult_meal_subtotal=(price_meal_adult + adult_drink) * number_adult
child_adult_subtotal=child_meal_subtotal + adult_meal_subtotal
print('\n')

print(f'The Subtotal for the meal is: ${child_adult_subtotal:.2f}')
sales_tax=(child_adult_subtotal * tax)/100
print(f' The sales tax: ${sales_tax:.2f}')

total_meal_price=sales_tax + child_adult_subtotal
print(f'Total Price for the Meal: ${total_meal_price:.2f}')
payment=float(input('How much are you paying: $'))
#customer_payment=payment
change=payment - total_meal_price
print(f' Your Change is: ${change:.2f}')
print('\n')

# I bid farewell to the user
print('Have A Nice Day')