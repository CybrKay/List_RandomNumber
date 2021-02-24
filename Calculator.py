# Project Name: Calculator
# Create Menu by select_menu function
def select_menu():
    print("1) sum")
    print("2) subtract")
    print("3) multiply")
    print("4) divide")
    print("0) Exit Program")


def sum ( number1, number2) :      # sum function for add two numbers
    result= number1 + number2
    print("The sum result is: %2d" %result)


def subtract ( number1 , number2):   # subtract function for subtract two numbers
    result= number1 - number2
    print("The subtract Result is: %2d" %result)


def multiply ( number1 , number2):   #multiply function for multiplication two numbers
    result= number1 * number2
    print("The Multiplication is: %2d" %result)


def divide (number1 , number2):     # divide function for division two numbers
    result=number1 / number2
    print("The division result is: %2d" %result)


# Sum=1
# Subtract=1
# Multiply=1
# Divide=1
select_menu()
options = int(input("please choose your option: "))
while options != 0:
    if options == 1:
        number1 = int(input("please enter number1: "))
        number2 = int(input("please enter number2: "))
        sum(number1, number2)

    elif options == 2:
        number3 = int(input("Please enter number1: "))
        number4 = int(input("Please enter number2: "))
        subtract(number3 , number4)

    elif options == 3:
        number5 = int(input("Please enter  number1: "))
        number6 = int(input("Please enter number2: "))
        multiply(number5 , number6)

    elif options == 4:
        number7 = int(input("Please enter number1: "))
        number8 = int(input("Please enter number2: "))
        divide(number7, number8)

    else:
        print("You chosen invalid option")
    print()
    select_menu()
    options = int(input("please choose your option: "))
print("thanks for your interaction")
