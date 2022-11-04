print("Hello world")
number = input("Enter a number: ")
number2 = input("Enter another number: ")
sign = input("Enter an operator sign: ")


def operator(sign):
    if sign == "+":
        print(int(number) + int(number2))
    elif sign == "-":
        print(int(number) - int(number2))
    elif sign == "*":
        print(int(number) * int(number2))
    elif sign == "/":
        print(int(number) / int(number2))
    else:
        print("Invalid Operation")


operator(sign)

