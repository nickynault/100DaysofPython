import art


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(art.logo)


def calculator():
    x = float(input("What's the first number?: "))
    for sign in operations:
        print(sign)
    operation_sign = input("Pick an operation from the line above: ")
    y = float(input("What's the second number?: "))
    calc = operations[operation_sign]
    answer = calc(x, y)

    print(f"{x} {operation_sign} {y} = {answer}")
    x = answer
    choice = input("Type 'y' to continue calculating or type 'n' to start a new calculation: ").lower()

    while choice == "y":
        operation_sign = input("Pick an operation again: ")
        y = int(input("What's the next number?: "))
        for sign in operations:
            print(sign)
        calc = operations[operation_sign]
        answer = calc(x, y)

        print(f"{x} {operation_sign} {y} = {answer}")
        x = answer
        choice = input("Type 'y' to continue calculating or type 'n' to start a new calculation (or 'e' to exit): ").lower()
    if choice == "n":
        calculator()
    elif choice == "e":
        exit()


calculator()
