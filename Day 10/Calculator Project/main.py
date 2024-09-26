
import art

print(art.logo)

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


proceed = "no"
first_number = 0
second_number = 0
result = 0

while True:
    if proceed == "no":
        first_number = int(input("Enter first number: "))
    operator = input('Enter mathematical operator ("+", "-", "*" or "/"): ')
    second_number = int(input("Enter second number: "))
    if proceed == "no":
        result = operation[operator](first_number, second_number)
    else:
        result = operation[operator](result, second_number)
    print(first_number)
    print(second_number)
    print(result)

    proceed = input("Do you want to continue work with previous result? (yes/no) ")
    second_number = 0
