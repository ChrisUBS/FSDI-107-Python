# Function
def menu():
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    return choice

# Call the function
while True:
    choice = menu()
    if choice == 5:
        break
    if choice == 1:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"{num1} + {num2} = {num1 + num2}")
    elif choice == 2:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"{num1} - {num2} = {num1 - num2}")
    elif choice == 3:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"{num1} * {num2} = {num1 * num2}")
    elif choice == 4:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Invalid choice")