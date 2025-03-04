### tip calculator
print("Welcome to tip calculator")
bill = float(input("Enter your total bill amount (INR) :"))
tip = float(input("Enter your tip percentage. 10, 15 or 20 % ? :"))
tip_amount = round((bill*tip)/100,2)
total_bill = round(bill+tip_amount,2)
persons = int(input("How many people are sharing the bill? :"))
print(f"Total bill is (including tip {tip}) : {total_bill}, with tip amount {tip_amount}")
print(f"Bill for per person {total_bill/persons}, for {persons} people")