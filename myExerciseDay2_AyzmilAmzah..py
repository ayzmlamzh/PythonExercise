# # Exercise 1
# # Add the loop and iteration for Day 1 Exercise 5 , and stop when don't want to ask the age
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

# while True:
#     user_age = int(input("Enter your age (or -1 to stop): "))
#     age_category = determine_age_category(user_age)
#     print("You are in the '"+ age_category +"' age category.")
    
#     if user_age == -1:
#         print("Exit program.")
#         break

# # Exercise 2
# # Print the multiplication table for the number from 1 to 10 with int input.

# num=int(input("Enter a number: "))
# print ("The multiplication table for ", num)
# for i in range(1,11):
#     result = num * i
#     print(i, "x",  num , "=" ,result)

# Exercise 3
# Write a small program about order food menu
    # 1. Display menu (food | price)
    # Loop
    # 2. User input - Food Order - Qty
    # 3. Calculation
    # 4.Display total (Total include discount)
    # Condition statement
    # Fx 
    # f-string

makanan = ["NL Biasa", "NL Ayam Goreng", "NL Sambal Kerang", "NL Gulai Udang", "NL Ikan Keli"]
harga = [3.00, 6.00, 6.50, 7.00, 7.50]

# function to display the menu
def display_menu():
    print("Menu:")
    for i, food in enumerate(makanan, start=1):
        print(f"{i}. {food} - RM{harga[i-1]:.2f}")

# function to calculate total cost with discount
def calJumKos(order, first_time=False):
    jumKos = sum(harga[i-1] * order[i] for i in order)
    if first_time:
        jumKos *= 0.85  # 15% discount for first-time orders
    return jumKos

# function to get yes/no input
def getYesNo_input(prompt):
    while True:
        response = input(prompt + " (Y/N): ").lower()
        if response in {'y', 'n'}:
            return response == 'y'
        else:
            print("Invalid input. Please enter 'Y' for yes or 'N' for no.")

# function to order
def orderMakanan():
    order = {}
    firstTimeOrder = getYesNo_input("Is this your first time ordering?")

    while True:
        display_menu()

        pilihan = input("Enter the number of the item you want to order (or 'q' to quit): ")
        
        if pilihan.lower() == 'q':
            break

        if pilihan.isdigit() and 1 <= int(pilihan) <= len(makanan):
            qty = int(input("Enter the quantity: "))
            order[int(pilihan)] = qty
            print(f"{makanan[int(pilihan)-1]} x {qty} added to your order.")

            if firstTimeOrder:
                print("Congratulations! You've received a 15%\ discount on your first order\.")
                firstTimeOrder = True

        else:
            print("Invalid choice. Please enter a valid item number.")

    jumKos = calJumKos(order, firstTimeOrder)
    print(f"Your total order cost is: RM{jumKos:.2f}")

orderMakanan()



      

     


