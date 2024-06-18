#Reversing a Strring
word="Hakuna Matata"

def reverse_string(word):
    my_string=""
    for char in word:
        my_string=char+my_string
    return my_string

print(f"The reverse_string is {reverse_string(word)}")