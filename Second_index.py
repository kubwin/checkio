def second_index(text: str, symbol: str):
     k=0
     for i in range(len(text)):
         if text[i]==symbol:
             k+=1
             if k==2:
                 return i
     return None
print(second_index("hi mr Mayor", " "))