import random 
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['@','#','$','&','?','!','(',')','+']
print("Welcome to password generator! ")
nr_letters=int(input("How many letters you like in your password? "))
nr_symbols=int(input("How many symbols you like in your password? "))
nr_numbers=int(input("How many numbers you like in your password? "))
password=[]
for i  in range(0,nr_letters):
    password.append(random.choice(letters))
for i  in range(0,nr_numbers):
    password.append(random.choice(numbers))
for i  in range(0,nr_symbols):
    password.append(random.choice(symbols))
random.shuffle(password)
print("your password can be ",end=" ")
for value in password:
    print(value,end="")    