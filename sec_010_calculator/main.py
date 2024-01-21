from art import logo

# add
def add(n1, n2):
    return n1 + n2

# substract
def substract(n1, n2):
    return n1 - n2

# multiply
def multiply(n1, n2):
    return n1 * n2

# divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    num2 = float(input("What's the second number?: "))
    for symbol in operations:
        print(symbol)
    chosen_operation = input("What operation, from line above do you want to use?: ")
    answer = operations[chosen_operation](num1, num2)
    print(f"{num1} {chosen_operation} {num2} = {answer}")
    continue_calculation = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")
    while continue_calculation == "y":
        chosen_operation = input("Pick an operation: ")
        num3 = float(input("What's the next number?: "))
        new_answer = operations[chosen_operation](answer, num3)
        print(f"{answer} {chosen_operation} {num3} = {new_answer}")
        answer = new_answer
        continue_calculation = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")
    calculator() # recursion

calculator()