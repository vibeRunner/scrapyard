# by m81v4n
import string

alphabet = list(string.ascii_uppercase)
text = input('Text: ').upper()
mode = int(input('1 to cipher, 2 to decipher:'))
brute = int(input('1 for BRUTE mode, 0 when key is known: '))

def cipher(i):
    global text
    out = ''
    for word in text.split(' '):
        for key in word:
            if key in alphabet:
                if alphabet.index(key) + i < len(alphabet):
                    out += alphabet[alphabet.index(key)+i]
                else:
                    out += alphabet[alphabet.index(key)+i-len(alphabet)]
            else:
                out += key
        if text.split(' ').index(word) != len(text.split(' ')):
            out += ' '
    return out

def decipher(i):
    global text
    out = ''
    for word in text.split(' '):
        for key in word:
            if key in alphabet:
                if alphabet.index(key) - i > 0:
                    out += alphabet[alphabet.index(key) - i]
                else:
                    out += alphabet[alphabet.index(key) - i]
            else:
                out += key
        if text.split(' ').index(word) != len(text.split(' ')):
            out += ' '
    return out

if mode == 1:
    if brute == 1:
        for i in range(len(alphabet)):
            print(cipher(i+1))
            print()
    elif brute == 0:
        print(cipher(int(input('i: '))))
elif mode == 2:
    if brute == 1:
        for i in range(len(alphabet)):
            print(decipher(i+1))
            print()
    elif brute == 0:
        print(decipher(int(input('i: '))))

### TODO:
# implement word checking for brute force and give results containing words, if none then all results