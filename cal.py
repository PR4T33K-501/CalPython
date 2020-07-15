# This is a Basic Calculatot

print("\033[34m" + "--------------------------------------------------")
print("\033[31m" + "   _____      _ _____       _   _                 ")
print("  / ____|    | |  __ \     | | | |                ")
print(" | |     __ _| | |__) |   _| |_| |__   ___  _ __  ")
print(" | |    / _` | |  ___/ | | | __| '_ \ / _ \| '_ \ ")
print(" | |___| (_| | | |   | |_| | |_| | | | (_) | | | |")
print("  \_____\__,_|_|_|    \__, |\__|_| |_|\___/|_| |_|")
print("                       __/ |                      ")
print("                      |___/                       ")
print("\033[34m" + "--------------------------------------------------")
print("\033[32m" + "        <====[[Coded By PR4T33K-501]]====>        ")
print("\033[34m" + "--------------------------------------------------")
print("\033[37m")
def add(x, y):
    return x + y 
def subtract(x, y):
    return x - y 
def multiply(x, y):
    return x * y 
def divide(x, y):
    return x / y
print("                                                 ")
print("         <-------------------------->            ")
print("          *** Choose calculation ***             ") 
print("         <-------------------------->            ")
print("                                                 ")
print("(1) +")
print("(2) -") 
print("(3) *") 
print("(4) /") 
print("                                                 ")
print("\033[34m" + "--------------------------------------------------")
choice = input("\033[32m" + "please input your choice(1 or 2 or 3 or 4): ") 
print("\033[34m" + "--------------------------------------------------")
print("\033[37m")
num1 = int(input("Enter The First Number: ")) 
num2 = int(input("Enter The Second Number: "))
print("                                                 ")
if choice == '1': print("Your answer is" , add(num1,num2),".") 
elif choice == '2': print("Your answer is" , subtract(num1,num2),".") 
elif choice == '3': print("Your answer is" , multiply(num1,num2),".")
elif choice == '4': print("Your answer is" , divide(num1,num2),".") 
else: 
    print("Invalid Operation!")    
