# Exercise 1
# 1. user input (ask birthday date).
# 2. calculate the age of user.
# 3. save the information to the file and read file.
# Main Method : Date and Time function and File Handling


from datetime import datetime
bd = input("Do input your birthday in a format of DD/MM/YYYY : ")
bd = datetime.strptime(bd, "%d/%m/%Y")
today = datetime.now()
age = today.year - bd.year 
print(f"You are {age} years old.")
f = open("YOUR AGE!.txt","x")
f.write(f"Birthday: {bd.strftime('%d/%m/%Y')}\n")
f.write(f"Your age is {age} years old.")






