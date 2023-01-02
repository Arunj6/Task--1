

#Display Fibonacci series up to n terms

num0 = int(input("Enter the Fibonacci sequence to display :"))  

num1, num2 = 0, 1

print("Fibonacci sequence:")

for i in range(num0):
    
    print(num1 , end="  ")
    
    res = num1 + num2

    num1 = num2
    num2 = res
print( "\n")