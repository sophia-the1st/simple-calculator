# calculator that performs simple operations on 2 operands
OPERATIONS = {
    1: "Addition",
    2: "Subtraction",
    3: "Multiplication",
    4: "Division",
}


def main():
    load_calc()
    
    operation = select_operation()
    
    num1 = enter_operand()
    print(f"\nNum 1 = {num1}")
    num2 = enter_operand()
    print(f"\nNum 2 = {num2}")
    
    result = perform_calculation(num1, num2, operation)
    
    display_result(num1, num2, operation, result)
    
    
def load_calc():
    print("Calculator".upper().center(20, "="))
    
    
def show_operations():
    print("\nAvailable operations:\n")
    for index, operation in OPERATIONS.items():
        print(f"{index})\t{operation.capitalize()}")
        
        
def select_operation():
    valid_entries = [str(index) for index in OPERATIONS.keys()]
    
    show_operations()
    
    while True:
        user_operation = input("\nSelect operation. (" + ", ".join(valid_entries) + ")\n>>> ").strip()
        
        if user_operation in valid_entries:
            return user_operation
        else:
            print("\nInvalid entry. Please enter (" + ", ".join(valid_entries) + "). Try again.\n")
            
            
def enter_operand():
    while True:
        operand = input("\nEnter a valid number.\n>> ").strip()
        if is_number(operand):
            return float(operand)
        else:
            print("\nPlease enter a valid number.")
    
     
def is_number(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
        
        
def perform_calculation(num1, num2, operation):
    match operation:
        case "1":
            return add(num1, num2)
        case "2":
             return subtract(num1, num2)
        case "3":
             return multiply(num1, num2)
        case "4":
             return divide(num1, num2)
        case _:
            print("\nInvalid operation.")
            
            
def add(num1, num2):
    return num1 + num2
    
    
def subtract(num1, num2):
    return num1 - num2
    
    
def multiply(num1, num2):
    return num1 * num2
    
    
def divide(num1, num2):
    return num1 / num2
            
            
def display_result(num1, num2, operation, result):
    print("\nResult:\n")
    match operation:
        case "1":
            print(f"\n{num1} + {num2} = {result}\n")
        case "2":
            print(f"\n{num1} - {num2} = {result}\n")
        case "3":
            print(f"\n{num1} * {num2} = {result}\n")
        case "4":
            print(f"\n{num1} / {num2} = {result}\n")
        case _:
            print("\nInvalid operation.")
    
    
if __name__ == "__main__":
    main()
