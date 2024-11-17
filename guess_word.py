from random_word import RandomWords
r=RandomWords()
word=r.get_random_word()


length=len(word)
print("Guess the Word : ",end="")
for i in range(length):
    print("_ ",end="")
print("")
display=""
done=False 
lifes=0
correct=0
correct_letters=[]

while not done:
    yes=0
    display=""
    guess=input("Guess a word : ")
    for i in word:
        if guess==i:
            display+=guess
            correct_letters.append(guess)
            correct+=1
            yes=1
        elif i in correct_letters:
            display+=i
        else:
            display+="_"
    print(display)        
    if correct==length:
            done=True
            print("YOu win")
    elif lifes==6:
        done=True
        print(f"YOu LOose.The Word was {word}")
    elif yes==0:
        lifes+=1
        print(f"You Lost a Life. Lifes Used {lifes}/6")   