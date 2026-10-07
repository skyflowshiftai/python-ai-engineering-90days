#Checking whether the user is eligible for voting or not?

print("====================================================")
print("      Positive - Negative - Zero Checker          ")
print("====================================================")

#Get the input from the user
age=int(input("Enter your age to check whether you are eligible for voting or not:"))

#checking the given age is eligible for voting or not?

if age>=18:
    print("The given age is eligible for voting!")
else:
    print("The given age is not eligible for voting!")
