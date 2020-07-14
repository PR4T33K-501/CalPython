def add(x, y):
    return x + y 
def subtract(x, y):
    return x - y 
def multiply(x, y):
    return x * y 
def divide(x, y):
    return x / y
print(" Choose calculation ") 
print("1 +")
print("2 -") 
print("3 *") 
print("4 /") 
choice = input("please input your choice(1 or 2 or 3 or 4):") 
num1 = int(input("please input a number: ")) 
num2 = int(input("please input a number : "))
if choice == '1': print(num1,"+",num2,"=", add(num1,num2)) 
elif choice == '2': print(num1,"-",num2,"=", subtract(num1,num2)) 
elif choice == '3': print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4': print(num1,"/",num2,"=", divide(num1,num2)) 
else: 
    print("error")    
