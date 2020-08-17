# by m81v4n
# special thanks to Caesar I guess

import string

alphabetUpper = list(string.ascii_uppercase)
alphabetLower = list(string.ascii_lowercase)

text = input('Text: ')
mode = int(input('1 to cipher, 2 to decipher: '))
brute = int(input('1 for BRUTE mode, 0 when key is known: '))


def caesarLoop(mode, i):

    global text
    out = ''

    for key in text:

        if key in alphabetUpper:
            out += mode(alphabetUpper, key, i)

        elif key in alphabetLower:
            out += mode(alphabetLower, key, i)

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


if mode == 1:

    if brute == 1:
        for i in range(26):  # 26x for EN
            print(caesarLoop(cipher, i + 1) + '\n')

    elif brute == 0:
        print(caesarLoop(cipher, int(input('i: '))))

elif mode == 2:

    if brute == 1:
        for i in range(26):  # 26x for EN
            print(caesarLoop(decipher, i + 1) + '\n')

    elif brute == 0:
        print(caesarLoop(decipher, int(input('i: '))))
