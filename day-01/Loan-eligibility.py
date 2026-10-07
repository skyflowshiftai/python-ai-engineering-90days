#BUILD A PYTHON PROGRAM FOR A SMALL BUSINESS LOAN ELIGIBILITY SYSTEM

age=int(input("Enter your age:"))
monthly_income=int(input("Enter your monthly income:"))
credit_score=float(input("Enter your credit score:"))
monthly_debit=float(input("Enter your monthly existing debt:"))
year_in_business=int(input("Enter the number of years in business:"))
defaulted=str(input("Select the applicant has defaulted before(Yes/No):"))

if age<21 and credit_score<600 and defaulted=="yes":
    print("Loan Denied!")
else:
    print("Calculation debt ratio!")

debt_ratio=monthly_debit/monthly_income

if monthly_income>=100000 and credit_score>=750 and debt_ratio<=0.30 and year_in_business>=3:
    print("You are eligible for premium approval!")
else:
    print("")

if monthly_income>=50000 and credit_score>=650 and debt_ratio<=0.45 and year_in_business>=1:
   print("You are eligible for standard approval!")
else:
    print("")

print("applicant does not qualify for either approval level but was not immediately rejected!")

