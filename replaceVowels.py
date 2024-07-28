word=input("Please enter a word: ")

newword=""

for letter in word:
	if letter in("a","e","i","o","u"):
		newword=newword+"_"
	else:
		newword=newword+letter

print(newword)