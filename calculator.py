print("Calculator")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("1 - Add")
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")

operation = input("Choose an operation: ")

if operation == "1":
    print("Result:", num1 + num2)
elif operation == "2":
    print("Result:", num1 - num2)
elif operation == "3":
    print("Result:", num1 * num2)
elif operation == "4":
    print("Result:", num1 / num2)
else:
    print("Invalid option")
