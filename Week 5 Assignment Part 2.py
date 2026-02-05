# I give the shopping cart a name 
print('~~~~Welcome to Shoprite®~~~~\n')

print('The Best Place to you can shop without regret\n')

#info to the user on how he is going to enter the options
print('•This is our shopping cart, Please choose any of the options by entering a number.')
print('• If you choose option one, please type the name of the item you want to add and it will be added for you')
print('• Option two is for viewing the content of your cart')
print('• In option three you will be instructed to enter the number in which the choice you wanted to remove belong to. If you entered a wrong choice you will be prompted again to enter the right choice')
print('• Option four is for viewing the total price of items in your shopping cart')
print('• Option five is for qutting, but i know you wont quit without shopping to your satisfaction')

# The lists variable for saving items and there prices respectively
items = []
prices = []

#The variable for item and price
item = ' '
price = 0

#variable for request
request = 0

#variable for the options
one = 1
two = 2
three = 3
four = 4
five = 5

#variable for total
total_price = 0

#variable for remove
remove = 0

while request != five:
    print('\nPlease select one of the Following:')
    print('1. Add Item')
    print('2. View Cart')
    print('3. Remove Item')
    print('4. Compute Total')
    print('5. Quit\n')
    
    #The first option
    request= int(input('Please enter an action? '))
    
    # The if statement for option one for adding items
    if request == one:
        item = input('\nWhich item did you want to add? ')
        # I put dollar sign infront of the item here
        price = float(input(f"\nWhat is the price of '{item.capitalize()}'? $"))
        
        #append function for adding items to the list
        items.append(item)
        prices.append(price)
        
        # I indicate both the item and the price that is been added to the cart here
        print(f"\n'{item.capitalize()}' with the the price '${price:.2f}' has been added to the cart")
    
    #The if statement for option two for viewing items in the shopping cart
    if request == two:
        print('\nThe contents of the shopping cart are:')
        for i in range(len(items)):
            list_item = items[i]
            list_price = prices[i]
            print(f'{i+1}. {list_item.capitalize()} -  ${list_price:.2f}')   
    
    #The if statement for option four for calculating the total price
    if request == four:
        for number in prices:
            total_price += number
        # To print this total once in a summed up manner the print statement must come out of this for loop
        print(f'\nThe Total price of items in the Shopping Cart is: ${total_price:.2f}')   
    
    #if statement for option five
    if request == five:
        print('\nThank You for shopping with us Goodbye')              

    # The if statement for option three if the user input the wrong choice
    if request == three: 
        remove = int(input('\nWhich item would you like to remove? '))
        while remove > len(items):
            print('\nYou have entered the wrong choice, please enter the right choice') 
            remove = int(input('\nWhich item would you like to remove? '))
            
        # The nested if statement if user enters the right choice
        if remove <= len(items):
            items.pop(remove - 1)
            prices.pop(remove - 1)
            print('\nItem removed')    