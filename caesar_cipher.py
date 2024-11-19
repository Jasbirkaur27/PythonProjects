logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

direction=input("Type you want to encode or decode ")
text=input("Type Your message: ").lower()
shift=int(input("Type the shift number: "))

def encrypt(encode_text, shiftt):
    secret=""
    for letter in encode_text:
        shifted_index = alphabet.index(letter)+shiftt
        shifted_index %= len(alphabet)
        secret += alphabet[shifted_index]
    print(secret)   
#encrypt(encode_text=text, shiftt=shift)

def decrypt(decode_text,shiftt):
    secret=""
    for letter in decode_text:
        shifted_index=alphabet.index(letter)-shiftt
        shifted_index %= len(alphabet)
        secret+=alphabet[shifted_index]
    print(secret)

def caesar(text,shiftt,encode_decode):
    secret=""
    if encode_decode=="decode":
        shiftt *= -1
    for letter in text:
        if letter in alphabet:
            shifted_index=alphabet.index(letter)+shiftt
            shifted_index %= len(alphabet)
            secret+=alphabet[shifted_index]
        else:
            secret+=letter
    print(f"your {encode_decode}d text is :",secret)
    
caesar(text=text, shiftt=shift, encode_decode=direction)
should_continue=True
while should_continue:
    response = input("Do you want to continue : Yes or No ").lower()
    if response=="no":
        should_continue=False
        print("Goodbye")
    else:    
        direction=input("Type you want to encode or decode ")
        text=input("Type Your message:").lower()
        shift=int(input("Type the shift number:"))
        caesar(text=text, shiftt=shift, encode_decode=direction)      
    
    
    
    