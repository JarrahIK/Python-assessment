## this will be a soultion to the furst problem which is returinng a dictionary with the following Number of characters
#Number of words
#Number of sentences
#Most common word
#Average word lenth
text = "Python is fun. Python is powerful."
def analyze_text (text:str)->dict:
 modified_text=text.split()
 number_of_char=0
 lengg=len(modified_text)
 for i in range(lengg):
    number_of_char+=len(modified_text[i])
 ana={
    "Number_of_words":lengg,
    "Number_of_char": number_of_char

 }
 return (ana)
print(analyze_text(text))



