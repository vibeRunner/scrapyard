import string
letterList = list(string.ascii_lowercase)
text = input().lower()
out = ""
for char in text:
	out += ((letterList.index(char)+1)*'ok').capitalize() if char in letterList else char
print(out)
