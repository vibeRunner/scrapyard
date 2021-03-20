# by vibeRunner
# special thanks to Caesar I guess

import string

alphabet_upper = list(string.ascii_uppercase)
alphabet_lower = list(string.ascii_lowercase)


def caesar_loop(text, mode, i):

    out = ''

    for key in text:

        if key in alphabet_upper:
            out += mode(alphabet_upper, key, i)

        elif key in alphabet_lower:
            out += mode(alphabet_lower, key, i)

        else:
            out += key

    return out


def cipher(alphabet, key, i):

    if alphabet.index(key) + i < len(alphabet):
        return alphabet[alphabet.index(key) + i]

    else:
        return alphabet[alphabet.index(key) + i - len(alphabet)]


def decipher(alphabet, key, i):

    if alphabet.index(key) - i > 0:
        return alphabet[alphabet.index(key) - i]

    else:
        return alphabet[alphabet.index(key) - i]


def main():

    text = input('Text: ')
    mode = int(input('1 to cipher, 2 to decipher: '))
    brute = int(input('1 for BRUTE mode, 0 when key is known: '))

    if mode == 1:

        if brute == 1:
            for i in range(1, 27):  # 26x for EN
                print(caesar_loop(text, cipher, i), end='\n\n')

        elif brute == 0:
            i = int(input('i: '))
            print(caesar_loop(text, cipher, i))

    elif mode == 2:

        if brute == 1:
            for i in range(1, 27):  # 26x for EN
                print(caesar_loop(text, decipher, i), end='\n\n')

        elif brute == 0:
            i = int(input('i: '))
            print(caesar_loop(text, decipher, i))


if __name__ == "__main__":
    main()
    
