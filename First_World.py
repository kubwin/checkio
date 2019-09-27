def first_word(text: str) -> str:
     t=0
     s=len(text)
     for i in range(s):
         if text[i]==" " or text[i]=="." or text[i]==",":
           t+=1
         else:
             break
     text = text[(t):s]
     s=len(text)
     for i in range(s-1,0,-1):
         if text[i]==" " or text[i]=="." or text[i]==",":
             text = text[0:(i)]
     return text
print(first_word(",.fb i, jh,. "))
