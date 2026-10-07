print("===============================================================")
print("                EMPLOYEE BONUS DECISION SYSTEM                ")
print("===============================================================")

# Get employee details
age = int(input("Enter the employee age: "))
performance_score = int(
    input("Enter the employee performance score (0-100): ")
)
years_at_company = int(
    input("Enter the number of years at the company: ")
)
number_of_absences = int(
    input("Enter the number of unexplained absences: ")
)
disciplinary_warning = input(
    "Did the employee receive a disciplinary warning? (Yes/No): "
).lower()

print("\n===============================================================")
print("                   EMPLOYEE INFORMATION                       ")
print("===============================================================")

print("Employee age:", age)
print("Performance score:", performance_score)
print("Years at company:", years_at_company)
print("Unexplained absences:", number_of_absences)
print("Disciplinary warning:", disciplinary_warning)

print("\n===============================================================")
print("                     FINAL DECISION                            ")
print("===============================================================")

# ---------------------------------------------------------------
# STEP 1: INPUT VALIDATION
# ---------------------------------------------------------------

if (
    age <= 0
    or performance_score < 0
    or performance_score > 100
    or years_at_company < 0
    or number_of_absences < 0
    or disciplinary_warning not in ["yes", "no"]
):
    print("Invalid input.")
    print("Please check the values entered.")

# ---------------------------------------------------------------
# STEP 2: IMMEDIATE DISQUALIFICATION
# ---------------------------------------------------------------

elif (
    performance_score < 50
    or disciplinary_warning == "yes"
    or number_of_absences > 10
):
    print("Decision: No Bonus")
    print("Reason: Employee is immediately disqualified.")

# ---------------------------------------------------------------
# STEP 3: PREMIUM BONUS
# ---------------------------------------------------------------

elif (
    age >= 21
    and performance_score >= 90
    and years_at_company >= 5
    and number_of_absences <= 3
):
    print("Decision: Premium Bonus")
    print("Reason: All premium bonus requirements are satisfied.")

# ---------------------------------------------------------------
# STEP 4: STANDARD BONUS
# ---------------------------------------------------------------

elif (
    performance_score >= 70
    and years_at_company >= 2
    and number_of_absences <= 7
):
    print("Decision: Standard Bonus")
    print("Reason: All standard bonus requirements are satisfied.")

# ---------------------------------------------------------------
# STEP 5: NEITHER BONUS LEVEL
# ---------------------------------------------------------------

else:
    print("Decision: No Bonus")
    print("Reason: Employee does not qualify for Premium or Standard bonus.")