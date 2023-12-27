# Exercise 1
# Create a meaningful variable name assign the value Apple to it.

# myFruit = 'Apple'
# print(myFruit)

# # Exercise 2
# # Get user input to display the age category using condition statement.
# age = int(input("Enter your age: "))

# if age < 0 or age > 99:
#  print("Invalid age entered.")
# elif age < 4:
#  print("You are in the 'Toddler' age category. ")
# elif age < 13:
#  print("You are in the 'Child' age category. ")
# elif age < 18:
#  print("You are in the 'Teenager' age category. ")
# elif age < 30:
#  print("You are in the 'Young Adult' age category. ")
# elif age < 50:
#  print("You are in the 'Adult' age category. ")
# else:
#  print("You are in the 'Senior' age category. ")

# #Exercise 3
# voltage = float(input("Enter the components voltage (in volts): "))

# if voltage < 3.0:
#   print("Low voltage")
# elif 3.0 <= voltage <= 3.6:
#   print("Standard voltage")
# else: 
#   print("High voltage")

# Exercise 4
# Create a calculate BMI function with the return value method.
def calculate_bmi(weight, height):
   
    # Calculate BMI (Body Mass Index) based on weight in kilograms and height in meters.

    if weight <= 0 or height <= 0:
        return "Invalid input."

    bmi = weight / (height ** 2)
    return bmi

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

result = calculate_bmi(weight, height)
# # f is a formatted string(f-string) can be used as a prefix before the string 
# print(f"Your BMI is: {result:.2f}")
print(f"Your BMI is: {result:.2f}") 
# print(f"Your BMI is: {result:.2f}")

# Exercise 5
# Create the function for Exercise 2
# def determine_age_category(age):
    
#     # Determine the age category based on the given age.
    
#     if age < 0 or age > 99:
#         return "Invalid age entered."
#     elif age < 4:
#         return "Toddler"
#     elif age < 13:
#         return "Child"
#     elif age < 18:
#         return "Teenager"
#     elif age < 30:
#         return "Young Adult"
#     elif age < 50:
#         return "Adult"
#     else:
#         return "Senior"

# user_age = int(input("Enter your age: "))
# age_category = determine_age_category(user_age)
# # print(f"You are in the '{age_category}' age category.")
# print("You are in the '"+ age_category +"' age category.")

# # Exercise 6
# # Define the function to check if a number is even or odd (User input)
# def check_even_odd(number):
    
#     # # Check if the given number is even or odd (using modulo).
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

#     # # Check if the given number is even or odd (not using modulo).
#     if (number // 2)*2 == number:
#         return "Even"
#     else: 
#         return "Odd"
    
# user_number = int(input("Enter a number: "))
# result = check_even_odd(user_number)
# # print(f"The number is {result}.")
# print("The number is: "+ result + ".")


