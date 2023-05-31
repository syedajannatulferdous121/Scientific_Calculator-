import math

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def power(num, exponent):
    return num ** exponent

def sqrt(num):
    return math.sqrt(num)

# Dictionary mapping operation names to corresponding functions
operations = {
    "1": ("Addition", add),
    "2": ("Subtraction", subtract),
    "3": ("Multiplication", multiply),
    "4": ("Division", divide),
    "5": ("Raise to the power of", power),
    "6": ("y to the power of x", power),
    "7": ("Square root", sqrt),
    "8": ("Exponential", math.exp),
    "9": ("Sine", math.sin),
    "10": ("Inverse sine", math.asin),
    "11": ("Cosine", math.cos),
    "12": ("Inverse cosine", math.acos),
    "13": ("Tangent", math.tan),
    "14": ("Inverse tangent", math.atan),
    "15": ("Log to the base of e", math.log),
    "16": ("Log base 10", math.log10),
}

# Main calculator loop
while True:
    print("Scientific Calculator Menu:")
    for key, value in operations.items():
        print(f"{key}. {value[0]}")
    print("Exit")

    choice = input("Enter the number corresponding to the desired operation: ")

    if choice.lower() == "exit":
        print("Exiting the calculator...")
        break

    if choice in operations:
        operation_name, operation_func = operations[choice]
        num1 = float(input("Enter the first number: "))

        # Handle square root and exponential operations separately
        if choice == "7" or choice == "8":
            result = operation_func(num1)
            print(f"Result: {operation_name} of {num1} = {result}")
        else:
            num2 = float(input("Enter the second number: "))
            result = operation_func(num1, num2)
            print(f"Result: {num1} {operation_name} {num2} = {result}")

    else:
        print("Invalid choice. Please enter a valid option.")
