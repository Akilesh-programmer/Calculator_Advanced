# Importing all the required things from all other files.
from art import logo
from functions import add
from functions import sub
from functions import multiply
from functions import divide
from functions import what_operation

# Some boolean expressions to carry the while loop.
new_calculation = True
continue_calculation = False

# Variables to store the result.
result = 0
previous_result = 0

# Putting the calculation under a while loop.
while new_calculation:
    # Printing the logo
    print(logo)
    # If the user wants to continue calculating from the previous result then storing that previous result as num1.
    if continue_calculation:
        num1 = previous_result
    # Getting the first number from user.
    else:
        num1 = int(input("What is the first number?: "))
    # Printing the symbols which the user needs to type in.
    what_operation()
    # Getting the operation that the user wants to perform.
    operation = input("What operation do you want to perform?: ")

    # Getting the second number from the user.
    num2 = int(input("What is the second number?: "))

    # Creating if and elif statements to do the calculation according to the symbol chosen by the user.
    if operation == "+":
        result = add(a=num1, b=num2)
    elif operation == "-":
        result = sub(a=num1, b=num2)
    elif operation == "*":
        result = multiply(a=num1, b=num2)
    elif operation == "/":
        result = divide(a=num1, b=num2)
    # Getting the user to know that they have typed the symbol wrong.
    else:
        print("You have made a typo in the operation input.")

    # Printing the result.
    print(result)

    # Asking the user whether they want to continue the calculation with the previous result or else they want new.
    what_next = input("Type 'n' to continue calculation with previous result. For new calculation type 'y'.")

    # Changing the while loop running statements according to the input from the user from what_next.
    if what_next == "n":
        continue_calculation = True
    else:
        new_calculation = True
    
    if what_next == "n":
        previous_result = result
