"""
ROT13 is a direct letter substitution cipher that substitutes a letter with the 13th letter in the alphabet after it. 
ROT13 is a variant of the Caesar cipher, which was created in ancient Rome.
"""

def rot13(message):
    res=''
    for letter in message:
        if letter.isupper():
            res+=chr(65+((ord(letter)-65+13)%26))
        elif letter.islower():
            res+=chr(97+((ord(letter)-97+13)%26))
        else:
            res+=letter
    return res