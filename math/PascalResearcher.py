"""
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
1 5 10 10 5 1

"""
prev = [1]
counter = 0
print("[1] 0")
while True:
    now = [1]
    for a in range(1,len(prev)+1):
        try:
            now.append(prev[a-1]+prev[a])
        except:
            now.append(1)
            break
    counter += 1
    print(now, counter)
    print("")
    prev = now
