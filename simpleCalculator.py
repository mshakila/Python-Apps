# Simple Calculator App

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b
    
def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


if __name__ == "__main__":
    print("calculator app")
    print('\n')
    print()
    
    num1 = int(input('Enter first number: '))
    num2 = int(input("Enter second number: "))
    
    choice = input("Enter your choice - add, sub, mul, div: ")
    print('-------------------------------------------------')
    add = 'add'.lower()
    sub = 'sub'.lower()
    mul = 'mul'.lower()
    div = 'div'.lower()
    
    
    if choice == 'add':
        print(f" The sum of {num1} & {num2} is {addition(num1,num2)}")
        
    elif choice == 'sub':
        print(f" The result of {num1} & {num2} is {subtraction(num1, num2)}")
        
    elif choice == 'mul':
        print(f" The product of {num1} & {num2} is {multiply(num1, num2)}")
        
    elif choice == 'div':
        try:
            if num2 != 0:
            print(f"The quotient of {num1} and {num2} is {divide(num1,num2}")    
        except ZeroDivisionError:
                print("zero division error")

    else: 
        print('Invalid input')
        
    print('--------------------------------------')
print("Visit again ! for more calculations !!!")
    
        
