def left_join(phrases):
    text=phrases[0]
    for i in range(1,len(phrases)):
        text+=","+phrases[i]
    text=text.replace("right","left")
    return text
print(left_join(("enough", "jokes")))