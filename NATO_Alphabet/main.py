import pandas
data = pandas.read_csv(r".\nato_phonetic_alphabet.csv")

phineotic={row.letter:row.code for (index,row) in data.iterrows()}
def generate_phonetic():
    word=input("Enter a word: ").upper()
    try:
        output_list=[phineotic[i] for i in word ]
    except KeyError:
        print("Sorry,only letters in alphabet please") 
        generate_phonetic()   
    else:
        print(output_list)
generate_phonetic()
