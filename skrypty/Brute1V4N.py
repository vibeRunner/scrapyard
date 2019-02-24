#by M81V4N
import string

### character list making
punctation = string.punctuation [::-1]
digits = string.digits [::-1]
letters = string.letters [::-1]
chars = list(punctation + digits + letters)
chars.append("")
chars.reverse()

### welcome text
print("""
- - - B R U T E   I V A N - - -

V E R S I O N :  A L P H A

2 0   c h a r a c t e r s   m a x
""")

password = "123"

raw_input("\nP R E S S   [ E N T E R ]   T O   B E G I N")

##### THE GREAT LOOP
####1 the first place of list is "", that means everything starts from nothing
####2 later every search is added and compared to password
####3 +1 to first search. If number > number of things in list, +1 to next search etc.
####4 repeat from 2.
for search0 in chars:
    for search1 in chars:
        for search2 in chars:
            for search3 in chars:
                for search4 in chars:
                    for search5 in chars:
                        for search6 in chars:
                            for search7 in chars:
                                for search8 in chars:
                                    for search9 in chars:
                                        for search10 in chars:
                                            for search11 in chars:
                                                for search12 in chars:
                                                    for search13 in chars:
                                                        for search14 in chars:
                                                            for search15 in chars:
                                                                for search16 in chars:
                                                                    for search17 in chars:
                                                                        for search18 in chars:
                                                                            for search19 in chars:
                                                                                now = search0 + search1 + search2 + search3 + search4 + search5 + search6 + search7 + search8 + search9 + search10 + search11 + search12 + search13 + search14 + search15 + search16 + search17 + search18 + search19
                                                                                print(
                                                                                    now)
                                                                                if now == password:
                                                                                    print("\n{ ! ! ! }   P a s s   f o u n d   { ! ! ! }")
                                                                                    print(now)
                                                                                    print("{ ! ! ! }   P a s s   f o u n d   { ! ! ! }")
                                                                                    exit("by M81V4N")

print("\nPassword not found."
      "\nIt may be bigger than 20 letters."
      "\nThe combination we ended on:\n"
      "~~~~~~~~~~~~~~~~~~~~~"
      "\nThat means the last possible of 20 letters.")
