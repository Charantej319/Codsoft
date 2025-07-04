#simple calculator
def menu():
    while(True):
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Exit")
        option = int(input("Choose an Operation :"))
        result = 0
        if(option in [1,2,3,4,5,]):
            num1 = float(input("Enter first number :"))
            num2 = float(input("Enter second number :"))

            if(option == 1):
                result = num1 + num2
            elif(option == 2):
                result = num1 - num2
            elif(option == 3):
                result = num1 * num2
            elif(option == 4):
                result = num1 / num2
            elif(option == 5):
                result = num1 ** num2
        elif(option == 6):
            exit()
        

        else:
            print("Invalid operation choosen...")

        print("the result of the operation : ",result)

menu()
