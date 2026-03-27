while True:
    print(" Calculator Menu ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("q. Quit")

    choice = input("Choose an option: ")

    if choice == "q":
        print("Calculator closed.")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    match choice:
        case "1":
            result = num1 + num2
            print("Result:", result)

        case "2":
            result = num1 - num2
            print("Result:", result)

        case "3":
            result = num1 * num2
            print("Result:", result)

        case "4":
            if num2 == 0:
                print("Cannot divide by zero!")
            else:
                result = num1 / num2
                print("Result:", result)

        case _:
            print("Invalid choice")