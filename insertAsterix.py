word=input("Please enter a word: ")

newword=""

for letter in word:
	if letter in("a","e","i","o","u"):
		newword=newword+letter+"*"
	else:
		newword=newword+letter

print(newword)


#or

word=input("Enter a word:")
newWord=""

for letter in word:
	newWord=newWord+letter
	if letter.lower() in "aeiou":
		newWord=newWord+"*"
print(newWord)