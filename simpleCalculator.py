# Simple Calculator App

def addNum(a,b):
    result = a+b
    return result

if __name__ == "__main__":
    print("Calculator App")
    
    print("\n")
    
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    choice = input("Enter add or sub or mul or div: ")
    print('-------------------------------------')
    if (choice == 'add'):
        result = num1 + num2
        #return result
        print(f"The sum of {num1} and {num2} is {result}")
    elif (choice == 'sub'):
        result = num1 - num2
        print(f"The result of {num1} and {num2} is {result}")
    elif (choice == 'mul'):
        result = num1 * num2
        print(f"The product of {num1} and {num2} is {result}")
    elif choice == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            print("zero division error")
        print(f"The quotient of {num1} and {num2} is {result}")
    else: 
        print('Invalid input')
        
    print('--------------------------------------')
print("Visit again ! for more calculations !!!")
    
        
