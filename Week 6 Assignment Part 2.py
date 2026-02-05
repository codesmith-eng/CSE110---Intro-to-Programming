# I gave the file a name
print('•••••Global Life Expectancy Program••••••\n\n')

#i inform the user of instruction to follow
print('• Welcome to the File of the Life Expectancy of people across the globe for the past 700 years\n')
print('• Input the Country and Year you want to know about there life expectancy, the maximum, minimum and average life expectancy of your input will be displayed for you\n')
print('• The overall Maximum and minimum life expectancy for the past 700 years will also be displayed for you\n')

# open the life expectancy.csv file
with open('/storage/emulated/0/Documents/Pydroid3/life-expectancy.csv') as file:
    #using readline function to through the firstline and cycling through the rest
    file.readline()
    
    
    #the initial variable for lowest and highest value in life expectancy of all the list
    lowest = 999999999999999999999999
    highest = 0
    
    #The initial variable for getting the overall max and min life expectancy and there years
    lowest_country = ' '
    highest_country = ' '
    lowest_year = ' '
    highest_year = ' '
    
    #The initial variable to determine the highest and lowest life expectancy of a country
    low = 9999999999999999999999
    high = 0
    
    #the initial variable for adding up the life expactancy of selected country and year
    total = 0
    totals = 0
    
    #the list for holding selected country and year in other to the get the length of the life expectancy of the selected country and year
    quantity = [ ]
    year_quantity =[ ]
    
    # The initial variable to calculate the highest life expectancy of a year
    high_year = 0
    country_year = ' '
    
    # The initial variable to calculate the lowest life expectancy of a year
    low_year = 99999999999999999999
    country_low = ' '
   
    country = input('Input the country of interest? ')   
    print()
    time = int(input('Enter the year of Interest? '))    
    
   # looping the file 
    for lines in file:
        #using the strip() to remove all spaces
        line = lines.strip()
        
        # splitting the file into four parts
        part = line.split(',')
        
        #The four parts
        entity = part[0]
        code = part[1]
        year = int(part[2])
        life_expectancy = float(part[3])
        #another part 4 for calculate the len of the life_expectancy in each country
        life = part[3]
        
        #The if statement to determine the lowest life expectancy value
        if life_expectancy < lowest:
            lowest = life_expectancy
            lowest_country = entity
            lowest_year = year
    
        # The if statement to determine the highest life expectancy value in the entire list
        if life_expectancy > highest:
            highest= life_expectancy
            highest_country = entity
            highest_year = year
            
         #The if statement to determine lowest life expectancy of a country
        if entity == country.capitalize():
            country = entity
            if life_expectancy < low:
                low = life_expectancy
    

#The if statement to determine highest life expectancy of a country
        if entity == country.capitalize():
            country = entity
            if life_expectancy > high:
                high = life_expectancy


#The if statement to determine the average life expectancy of a country
        if entity == country.capitalize():
            country = entity
            if life_expectancy != 0:
                #putting life_expectancy of the selected country into a list with the variable named quantity to get the length of the life_expectancy
                quantity.append(life_expectancy)
                len_quantity = len(quantity)
                total += life_expectancy
                average = total/len_quantity
                
       # The if statement to calculate the highest life expectancy of a year         
        if year == time:
               time = year
               if life_expectancy > high_year:
                   high_year = life_expectancy
                   country_year = entity
                   
       # The if statement to calculate the lowest life expectancy of a year                
        if year == time:
               time = year
               if life_expectancy < low_year:
                   low_year = life_expectancy
                   country_low = entity
               
#The if statement to determine the average life expectancy of a year
        if year == time:
            time = year
            if life_expectancy != 0:
                #putting life_expectancy of the selected year into a list with the variable named year_quantity to get the length of the life_expectancy
                year_quantity.append(life_expectancy)
                list_year = len(year_quantity)
                totals += life_expectancy
                average_year = totals/list_year           
    print(f'\nFor {country}:')         
    print(f'The lowest life expectancy for {country.capitalize()} is {low:.2f}')           
    print(f'The highest life expectancy for {country.capitalize()} is {high}')      
    print(f'The Average life expectancy for {country.capitalize()} is {average:.2f}')
    
       
    print(f'\n\nFor the year {time}:') 
    print(f'The average life across all countries was {average_year:.2f}')
    print(f'The maximum life expectancy was in {country_year} with {high_year}')  
    print(f'The minimum life expectancy was in {country_low} with {low_year}')  
    
                       
    print(f'\n\nThe overall minimum life expectancy is {lowest} from {lowest_country} in the year {lowest_year}')     
     
    print(f'The overall maximum life expectancy is {highest} from {highest_country} in the year {highest_year}\n')


print('\nThis Life Expectancy program was created by Moses, enjoy')

# I showed creativity by giving it a name and made it mine. 
# i also add instruction for the user

        
            
            
            