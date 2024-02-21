#first code
print("Hello World")




# variable declaration, inputs
# Input numbers
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

# Add two numbers
sum = int(num1) + int(num2)

# Display the sum
print("The sum of the numbers is :")
print(sum)




# conditional statements, F-string, Logical operators
# Python program to check if year is a leap year or not
year = int(input("Enter a year: "))

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
    print(f"{year} is a leap year")

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (year % 4 ==0) and (year % 100 != 0):
    print(f"{year} is a leap year")

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print(f"{year} is not a leap year")





#lists
list_1 = ['a', 'b']
list_2 = [3, 4, 5]

joined_list = list_1 + list_2
print(joined_list)


# Capitalize Words, functions
# Write a program that accepts a string as input, capitalizes the first letter of each word in the 
# string, and then returns the result string.
def Capitalize_words(words):
    words_list = words.split(' ')
    new_list = [word.capitalize() for word in words_list]
    return ' '.join(new_list) 

print("Enter a sentence: ")
words = input()
print(Capitalize_words(words))





# Program to generate a random number between 0 and 9
# importing the random module
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