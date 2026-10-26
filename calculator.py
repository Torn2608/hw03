def calculate(a, operator, b):
    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    elif operator == "*":
        result = a * b
    elif operator == "/":
        if b == 0:
            result = None
        else:
            result = a / b
    else:
        result = None
    return result


def main():
    first = input("First number (or q): ")
    while first != "q":
        op = input("Operator (+ - * /): ")
        second = input("Second number: ")
        a = float(first)
        b = float(second)
        answer = calculate(a, op, b)
        if answer == None:
            print("Cannot calculate that")
        else:
            print("Result:", answer)
        first = input("First number (or q): ")


if __name__ == "__main__":
    main()
