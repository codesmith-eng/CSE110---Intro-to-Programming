#LOAN CALCULATOR
#I welcome the user and prompt him/her to enter detals needed
print('Good day dear user, Welcome to Global loan')
print('Please enter the following details to check your qualifications for a loan')

# i prompt the user to enter values
first = input('first name: ')
middle = input('middle name: ')
last = input('last name: ')

large = float(input('how large is the loan: '))
credit_history = int(input('how good is your credit history (please enter a number on a rating of 1 - 10): '))
income = float(input('how large is your income: '))
down_payment = float(input('how large is your downpayment: '))

if (large >= 5 and credit_history > 4) and income == 7 or down_payment == 7 or (income == 4 and down_payment == 4):
    loan = True
else:
    loan = False
if loan:
    print('Congrats You have a loan')
else:
    print('You are not eligible for a loan')