#pig latin program

word = input("Enter a word: ")
first = word[0]
length = len(word)
rest = word[1:length]
if (first == "a" or "e" or "i" or "o" or "u"):
    newword = rest + first + "ay"
else:
    newword = word + "way"
print(newword.lower())

