def find_message(text):
    strt=""
    for i in range(len(text)):
        strt+=text[i]*text[i].isupper()
    return strt
print(find_message("HELLO WORLD!!!"))