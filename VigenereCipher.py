#VigenereCipher.py
import CaesarCipher

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def keywordToNumber(keyword):
    keyword = keyword.upper()
    keys = []
    for letter in keyword:
        key = alpha.find(letter)
        keys.append(key)

    return keys



def encode(message, keyword):
    secret = ""
    letterCount = 0
    keys = keywordToNumber(keyword)

    message = message.upper()
    for letter in message:
        key = keys[letterCount % len(keys)]

        #use the encode/decode methods from your Caesar Cipher.
        #The key will change for each letter so you'll be encoding
        #a one-letter phrase using the Caesar Cipher and adding the results together.


    return secret
