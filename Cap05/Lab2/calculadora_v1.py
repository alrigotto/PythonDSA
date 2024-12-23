# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

# Andre Luiz Rigotto em 26/11/2024

# Functions

def operation(oper, n1, n2): # make the operations
    if oper == 1:
        return n1 + n2
    elif oper == 2:
        return n1 - n2
    elif oper == 3:
        return n1 * n2
    elif oper == 4:
        return n1 / n2
    else:
        print("Invalid parameter!")

def operation_symbol(oper):
    if oper == 1:
        return "+"
    elif oper == 2:
        return "-"
    elif oper == 3:
        return "*"
    elif oper == 4:
        return "/"
    else:
        print("Invalid parameter!")

def is_float(value): #check if a value is a float (because Python doesn't have a ".isfloat" method)
    try:
        float(value)
        return True
    except ValueError:
        return False

def line_space(lines): # print space lines
    for i in range(lines):
        print()

def menu(): # print the operation menu
    print("1 - Sum")
    print("2 - Subtraction")
    print("3 - Product")
    print("4 - Division")

def converter_character(n): # convert the character in a float or int
    if n.isdigit():
        return int(n)
    elif is_float(n):
        return float(n)
    else:
        return n

def check_number(n): # Check if "n" is a string or a valid number (float or int)
    n_converted = converter_character(n)
    if type(n_converted) == str:
        return False
    else:
        return n_converted

def type_number(n): # get and check the numbers typed by user
    #if n == 1:
    while True:
        if n == 1:
            num = check_number(input("Type the first number: "))
            print()
        elif n == 2:
            num = check_number(input("Type the second number: "))
            print()
        else:
            print("Wrong parameter!")
        
        if num == False and type(num) == bool: # because 0 is false and it was needed to detect it indirectly. 
            print("You don't type a valid number! \n")
        else:
            return num

def type_operation(): # check if the chosen operation is valid
    operation = converter_character(input("Type your choice (1/2/3/4): "))
    print()
    while operation not in [1, 2, 3, 4]:
        print("Please, type a valid operation! \n")
        operation = converter_character(input("Type your choice (1/2/3/4): "))
        print()
    return operation


# Main ##############################################################################################

exit_calculator = 0
while exit_calculator == 0:
    line_space(3)
    print("\n******************* Calculator in Python *******************\n")
    print("Select the number of desired operation:\n")
    menu() # Show operation menu
    line_space(1)

    oper = type_operation() # get from user the operation number

    n1 = type_number(1)

    n2 = type_number(2)

    while oper == 4 and n2 == 0: # check division by zero
        print("You type 0. The operation is a Division! \n")
        n2 = type_number(2)

    symbol = operation_symbol(oper)
    calculate = operation(oper, n1, n2)

    print(n1, symbol, n2, " = ", calculate)

    print()


    while True:
        new_calculation = input("Would you like to make a new calculation? Yes (y) or N2ot (n): ")
        print()
        if new_calculation in ["n", "N"]:
            exit_calculator = 1
            print("Bye! Thank you!!! \n")
            break
        elif new_calculation in ["y", "Y"]:
            break
        else:
            continue













