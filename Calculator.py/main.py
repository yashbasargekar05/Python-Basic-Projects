try: 
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number:"))


    print("What kind of operation do you want to perfrom. Press + for addition\n Press - for subtraction\n Press * for multiplication\n Press / for division")

    o =input("Enter the operation :")
    match o:
        case "+":
            print(f"The sum of {a} and {b} is {a+b}")
        case "-":
            print(f"The difference of {a} and {b} is {a-b}")
        case "*":
            print(f"The product of {a} and {b} is {a*b}")
        case "/":
            if b == 0:
                print("Division by zero is not allowed.")
            else:
                print(f"The quotient of {a} and {b} is {a/b}")
        case _:
            print("Invalid operation. Please choose +, -, *, or /.")

except Exception as e:
    print("Enter valid value of a and b ")
    exit()