def checkio(number):
    text=str(number)
    sum=1
    for i in range(len(text)):
        sum*=int(text[i]) if int(text[i])!=0 else 1
    return sum
print(checkio(1111))