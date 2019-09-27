def checkio(words):
    t=0
    p=False
    a=words.split()
    for i in range(len(a)):
        if not a[i].isdigit():
            t+=1
            if t==3:
                p=True
        else:
            t=0
    return p

print(checkio("ergver oik 4 oim om"))