number = int(input("Enter a number (1-101): "))

if number < 1 or number > 101:
    print("Number must be between 1 and 101.")
else:
    factorial = 1

    for i in range(1, number + 1):
        factorial = factorial * i

    print("Factorial of", number, "is", factorial)