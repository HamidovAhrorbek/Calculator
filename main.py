def add(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


def multiply(number1, number2):
    return number1 * number2


def divide(number1, number2):
    return number1 / number2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print("Welcome to the calculator!")
    print("You can add (+), subtract (-), multiply (*) or divide (/) numbers.")
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = str(input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:"))

        if choice == 'y':
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()
