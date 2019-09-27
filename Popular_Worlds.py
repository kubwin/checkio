def popular_words(text, words):
    text=text.lower()
    dict1= {}
    for i in range(len(words)):
       dict1.update({words[i]: text.count(words[i])})
    return dict1
text="When I was One, I had just begun. When I was Two, I was nearly new."
words=['i', 'was', 'three']
print(popular_words(text, words))