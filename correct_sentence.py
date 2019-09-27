def correct_sentence(text: str) -> str:
   text=text.strip()
   s=len(text)
   text = text[0].upper()+text[1:(s)]
   if text[s-1]!=".":
       Newtext=text+"."
       return Newtext
   else:
       return text
print(correct_sentence(" greetings, friends "))