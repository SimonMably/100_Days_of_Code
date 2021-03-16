import pandas

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv", index_col=0,
                                squeeze=True).to_dict()

user_input = input("Type word or message and receive word/message in phonetic alphabet: ")

code_words = [nato_alphabet.get(letter.upper()) for letter in user_input if letter.upper() in nato_alphabet]
print(code_words)


