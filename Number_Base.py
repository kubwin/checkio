def checkio(str_number, radix):
    try:
        x= int(str_number, radix)
    except :
        x=-1
    return x
print(checkio("101",5))