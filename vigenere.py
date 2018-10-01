from helpers import alphabet_position, rotate_character
         
def encrypt(text, key):
    ans = ""ow 
    i = 0
    for letter in text:
        if letter.isalpha():
            ans += rotate_character(letter, alphabet_position(key[i%len(key)]))   
            i += 1                                    
        else:
             ans += letter
    return ans

def main():
    # your main code (input and print statements)
    userInput = input("Type a message:\n")
    key = input("Encryption key:\n")
    print(encrypt(userInput, key))

if __name__ == "__main__":
    main()