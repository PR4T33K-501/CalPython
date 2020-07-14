# This is a Basic Calculator
print ("This is a super Basic Calculator\n")
print ("Created By PR4T33K-501\n")
def add(x, y):
    return x + y 
def subtract(x, y):
    return x - y 
def multiply(x, y):
    return x * y 
def divide(x, y):
    return x / y
print("       Choose calculation\n ") 
print("(1) +")
print("(2) -") 
print("(3) *") 
print("(4) /") 
choice = input("please input your choice(1 or 2 or 3 or 4):\n") 
num1 = int(input("Enter Thw First Number: ")) 
num2 = int(input("Enter The Second Number: "))
if choice == '1': print(num1,"+",num2,"=", add(num1,num2)) 
elif choice == '2': print(num1,"-",num2,"=", subtract(num1,num2)) 
elif choice == '3': print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4': print(num1,"/",num2,"=", divide(num1,num2)) 
else: 
    print("error")    
