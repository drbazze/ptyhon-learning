from art import logo

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def devide(n1, n2):
    return n1 / n2

operations = {"+": add, "-": subtract, "*": multiply, "/": devide}

def calculator():
    """Make calculation based on the available operations"""
    #Print the Logo
    print(logo)

    #The first number input
    num1 = float(input("What's the first number? "))

    for symbol in operations:
        print(symbol)

    #Conditions for the loop
    continue_calculation = True
    valid_operation_input = True

    while continue_calculation and valid_operation_input:
        #The operation symbol input
        operation_symbol = input("Pick an operation: ")

        if operation_symbol in operations:
            num2 = float(input("What's the next number? "))

            operation_func = operations[operation_symbol]
            calculation_result = operation_func(num1, num2)
            print(f"{num1} {operation_symbol} {num2} = {calculation_result}")

            continue_calculation = input(f"Type 'y' to continue calculating with {calculation_result}, or type 'n' to exit.: ")

            if continue_calculation.lower() == "y":
                #Keep the actual calculation result
                num1 = calculation_result
            else:
                continue_calculation = False
                #Recursive call
                #TODO: a stop command would come handy
                calculator()
        else:
            valid_operation_input = False

    #Error handling for the operation
    if not valid_operation_input:
        print("Invalid operation")

#Call the main function
calculator()