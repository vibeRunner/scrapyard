#by M81V4N

#used on begining of loop
def refresh():
    import data as d
    data = d.data
    return data

#used after each file-changing process
def save():
    file = open("data.py","w")
    file.write("data = ")
    file.close()
    file = open("data.py", "a")
    file.write("[\n")
    for entry in data:
        file.write(str(entry))
        file.write(",\n")
    file.write("]")
    file.close()

#find database number by inputing name
def search():
    found = False
    name = raw_input("\nNAME: ")
    for num in range(0, len(data)):
        if (data[num]["name"]) == name:
            print("\nDATABASE LOCATION: "+str(num))
            print(data[num])
            found = True
    if found == False:
        print("Nothing found. PROTIP: search is case-sentitive and requires full words.")

#add new value to entry or change existing
def update():
    try:
        location = input("\n(type 'cancel' to cancel)\nDB LOCATION: ")
        keyword = raw_input("KEYWORD: ")
        value = raw_input("VALUE: ")
        try:
            value = int(value)
        except:
            value = str(value)
        data[location][keyword] = value
        save()
        print(data[location])
    except:
        print("Updating canceled.")
        
#add new entry
def append():
    name = raw_input("\nNAME: ")
    data.append({"name":name})
    save()
    print("New person added at DB Location " + str(len(data)-1))

#show all entrys
def smartList():
    print("\n")
    for num in range(0,len(data)):
        print("N0: " + str(num))
        for key in data[num]:
            print(key + ": " + str(data[num][key]))
        print("--")
    
##main loop that is command prompt
while True:
    data = refresh()
    command = raw_input("\n/")
    if command == "search" or command == "find":
        search()
    elif command == "list":
        smartList()
    elif command == "update" or command == "upd":
        update()
    elif command == "append" or command == "new":
        append()
    elif command == "exit":
        exit("\nclosed by user.\n\nscript by: M81V4N")
    else:
        print("Wrong command. Try again.")
        
        
        
