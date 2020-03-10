diz = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("test04a.txt", 'a') as agrob:
    with open("test04.txt", 'r+') as grob:
        ab = grob.read().split("\n")
        for i in ab:
            i = i.split(" — ")
            agrob.writelines(diz[i[0]] + " — " + i[1] + "\n")
