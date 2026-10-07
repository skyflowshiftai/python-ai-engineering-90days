#Check whether the given number is positive/Negative/Zero

print("====================================================")
print("      Positive - Negative - Zero Checker          ")
print("====================================================")

#Get the input from the user
number=int(input("Enter the number to check whether it is positive/Negative/Zero:"))

#checking the given number is positive or Negative or Zero

if number%2==0:
    print("The given number is positive!")
elif number%1==0:
    print("The given number is negative!")
else:
    print("The given number is zero!")
