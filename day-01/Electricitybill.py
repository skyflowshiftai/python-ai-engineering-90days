# ELECTRICITY BILL CALCULATOR

print("===================================")
print("    ELECTRICITY BILL CALCULATOR")
print("===================================")

#Get the details from the user
name=str(input("Enter the user name:"))
units_consumed=float(input("Enter the units consumed:"))

#total bill calculation

if units_consumed<=100:
    print("Your electricity bill is 5rs/unit!")
elif units_consumed>100 and units_consumed<=200:
    print("Your electricity bill is 7rs/unit!")
elif units_consumed>200:
    print("Your electricity bill is 10rs/unit!")
else:
    print("")

