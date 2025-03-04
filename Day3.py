#print(2.2/3)
# Odd or Even

# number = int(input("Enter number to check if it is odd or even :"))
# if number%2 == 0:
#     print("It is Even")
# else:
#     print("It is Odd")

weight = 62
height = 1.65

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi < 25:
    print("normal weight")
else:
    print("overweight")