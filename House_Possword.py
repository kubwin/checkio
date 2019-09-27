def checkio(data):
    a=True
    b=True
    c=True
    d=True
    e=True
    if len(data) < 10:
        a = False
        return a
    for i in range(len(data)):
       b=(not data[i].isdigit())*b
       c=(not data[i].islower())*c
       d=(not data[i].isupper())*d
       e=(not data[i].isalpha())*e
    if b+c+d+e>0:
        a=False
    return a

print(checkio('QWERTYqwerty'))
