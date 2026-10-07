#Comparing two number and check which is bigger

print("====================================================")
print("        Comparing two number and check which is       ")
print("                     Bigger Number                  ")
print("====================================================")

#Get the input from the user
num1=int(input("Enter the first number to compare:"))
num2=int(input("Enter the second number to compare:"))

#Comparing the two numbers

if num1>num2:
    print("The first number is bigger!")
elif num2>num1:
    print("The second number is bigger!")
else:
    print("The two numbers are equal!")