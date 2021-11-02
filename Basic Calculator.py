print("This program is a basic calculator, select an operation to perform")
print("1) Add")
print("2) Subtract")
print("3) Multiply")
print("4) Divide")

selection = int(input("Select the operation you want to perform: "))

if selection == 1:
    num1 = int(input('Please enter your first number: '))
    num2 = int(input('Please enter your second number: '))
    print("The answer is {}" .format(num1 + num2))


elif selection == 2:
    num1 = int(input('Please enter your first number: '))
    num2 = int(input('Please enter your second number: '))
    print("The answer is {}".format(num1 - num2))


elif selection == 3:
    num1 = int(input('Please enter your first number: '))
    num2 = int(input('Please enter your second number: '))
    print("The answer is {}".format(num1 * num2))


elif selection == 4:
    num1 = int(input('Please enter your first number: '))
    num2 = int(input('Please enter your second number: '))

else:
    print("Invalid Input")
