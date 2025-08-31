# Simple calculator 
print ("\n----------Calculator-------------")
try:
    a = int(input("Enter the first number: ")) # Enter the first number

    b = int(input("Enter the second number: ")) # Enter the second number 

    print("What kind of operation do you want to perform?\n Press '+' for addition\n Press '-' for subtraction\nPress'*' for multiplication\nPress'/' for division.")
    
    operation = input("Enter the operation: ") # Asking what type of operation you want to perform ex:- add,sub
    match operation:
        case "+":
            print(f"The result is : {a+b}")
        case "-":
            print(f"The result is : {a-b}")
        case "*":
            print(f"The result is : {a*b}")
        case "/":
            print(f"The result is : {a/b}")
        case default:
            print(f"There was an error")
except Exception as e:
    print("Enter a valid value of a and b")  