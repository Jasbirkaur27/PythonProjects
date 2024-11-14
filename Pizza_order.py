print("Welcome to Python pizza deliveries!")
size=input("What size do you want? S,M,L: ")
pepperoni = input("Do you want pepperoni on yoour pizza? Y or N: ")
extra_cheese = input("Do you want extra cheeze? Y or N :")
if size=='S':
    bill=15
elif size=='M':
    bill=20
else:
    bill=25
if pepperoni=='Y':
    bill+=2
if extra_cheese=='Y':
    bill+=1
print(f"Your final bill is {bill}") 