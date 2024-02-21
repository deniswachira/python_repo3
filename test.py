# # variable declaration, inputs
# # Input numbers
# num1 = input('Enter first number: ')
# num2 = input('Enter second number: ')

# # Add two numbers
# sum = int(num1) + int(num2)

# # Display the sum
# print("The sum of the numbers is :")
# print(sum)

# # conditional statements, F-string, Logical operators
# # Python program to check if year is a leap year or not
# year = int(input("Enter a year: "))

# # divided by 100 means century year (ending with 00)
# # century year divided by 400 is leap year
# if (year % 400 == 0) and (year % 100 == 0):
#     print(f"{year} is a leap year")

# # not divided by 100 means not a century year
# # year divided by 4 is a leap year
# elif (year % 4 ==0) and (year % 100 != 0):
#     print(f"{year} is a leap year")

# # if not divided by both 400 (century year) and 4 (not century year)
# # year is not leap year
# else:
#     print(f"{year} is not a leap year")

import random

print(random.randint(0,9))

def colors_game(day):
    colors = ("Blue", "Gray", "White","Red", "Pink", "Purple","Green", "Brown", "Beige","Black" )
    days = ( "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

    if day in days:
        # for color in colors:
           suggested_color = random.choice(colors)
           print(f"For {day}, suggested color to wear: {suggested_color}") 

    else:
        print("Invalid day. Please enter a valid day of the week.")

user_day = input("Enter today's day: ").capitalize()
# Call the function with the user-provided day
colors_game(user_day)