# Ask the user to enter two numbers.
first_input = input("Enter the first number: ")
second_input = input("Enter the second number: ")

# Attempt to convert both inputs into floating-point numbers.
try:
    first_number = float(first_input)
    second_number = float(second_input)

    # Ask the user which arithmetic operation to perform.
    operation = input("Choose an operation (+, -, *, /): ").strip()

    # Select and perform the requested operation.
    if operation == "+":
        result = first_number + second_number
        print(f"{first_number:g} + {second_number:g} = {result:g}")
    elif operation == "-":
        result = first_number - second_number
        print(f"{first_number:g} - {second_number:g} = {result:g}")
    elif operation == "*":
        result = first_number * second_number
        print(f"{first_number:g} * {second_number:g} = {result:g}")
    elif operation == "/":
        # Division by zero is not allowed.
        if second_number == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = first_number / second_number
            print(f"{first_number:g} / {second_number:g} = {result:g}")
    else:
        print("Error: Unsupported operation. Please choose +, -, *, or /.")

except ValueError:
    print("Error: Please enter valid numbers.")