#Ceasar Cypher
#100 Days of Code ! Day 8

alphabet=['a','b', 'c','d', 'e','f','g','h', 'i',
'j','k','l', 'm', 'n','o', 'p','q', 'r',
's','t','u', 'v', 'w','x', 'y','z']

#User inputs request
direction=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text=input("Enter text:\n").lower()
shift=int(input("Enter number of letter to shift:\n")) % 25

#function for encrypting or decrypting text
def ceasar(start_text,shift_amount,cypher_direction):
    end_text=""
    if cypher_direction=='decode':
        shift_amount*=-1
    print(cypher_direction)
    for letter in start_text:
        if letter in alphabet:
            position=alphabet.index(letter)
            new_position=(position+shift_amount) % 26
            end_text+=alphabet[new_position]
        else:
            end_text += letter
    
    print(end_text)

#function call
ceasar(start_text=text,shift_amount=shift,cypher_direction=direction)