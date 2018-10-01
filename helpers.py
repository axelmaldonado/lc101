def alphabet_position(letter):
    #letter = input("Rotate by:\n")
    if letter.isupper():
        return (ord(letter) - 65)
    elif letter.islower():
        return (ord(letter) - 97)
    else:
        return letter


def rotate_character(char, rot):
    if char.isupper():
        return chr(((alphabet_position(char) + rot) % 26) + 65)
    elif char.islower():
        return chr(((alphabet_position(char) + rot) % 26) + 97)
    else:
        return char