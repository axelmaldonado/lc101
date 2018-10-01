from helpers import alphabet_position, rotate_character
  
def encrypt(text, rot):
    ans = ""
    for letter in text:
        ans += rotate_character(letter, rot)
    return ans

def main():
    # your main code (input and print statements)
    userInput = input("Type a message:\n")
    userRot = int(input("Rotate by:\n"))
    print(encrypt(userInput, userRot))


if __name__ == "__main__":
    main()