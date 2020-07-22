import CaesarCipher
import VigenereCipher
import SubstitutionCipher
import Enigma

def main():
    #Caesar Cipher
    message = input("Enter a message: ")

    key = int(input("Enter a key: "))
    secret = CaesarCipher.encode(message, key)
    print ("Caesar Encrypted:", secret)

    #Vigenère Cipher
    #keyword = input("Enter keyword: ")
    #secret = VigenereCipher.encode(message, keyword)
    #print ("Vigenere Encrypted:", secret)

    #Substitution Cipher
    #key = input("Enter a key: ")
    #secret = SubstitutionCipher.encode(message, key)
    #print ("Substitution Encrypted:", secret)

    #Enigma Cipher
    #Enigma.setStart("A", "B", "C")
    #secret = Enigma.encode(message)
    #print ("Enigma Encrypted:", secret)

main()
