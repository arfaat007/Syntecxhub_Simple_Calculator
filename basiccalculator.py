def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    if b==0:
        return "Error! Division by zero."
    return a / b
def clear():
    print("Calculator cleared.")
    
def calculator():
    print("Welcome to the Basic Calculator!")
    print("Select operation:+, -, *, /")
    print("Type 'clear' to reset the calculator or 'exit' to quit.")
    while True:
        user_input = input("Enter operation: ").strip()
        
        if user_input.lower() == 'exit':
            print("Exiting the calculator. Goodbye!")
            break
        elif user_input.lower() == 'clear':
            clear()
            continue
        
        try:
            parts=user_input.split()
            if len(parts) != 3:
                print("Invalid input format. Please enter in the format: number1 operation number2")
                continue
            num1, operator, num2 = parts
            num1 = float(num1)
            num2 = float(num2)
            if operator == '+':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif operator == '-':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif operator == '*':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif operator == '/':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            else:
                print("Invalid operation. Please select from +, -, *, /.")
        except ValueError:
            print("Invalid numbers. Please enter valid numerical values.")

if __name__ == "__main__":
    calculator()
    