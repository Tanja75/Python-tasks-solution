#Program that reads words from user until blank then display each word entered only once in same order they were entered:
words=[]
word=input("Please enter words:")
while word!="":
    if word not in words:
        words.append(word)
    word=input("Please enter words: ")
for word in words:
    print(word)
