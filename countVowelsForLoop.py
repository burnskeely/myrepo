word=input("Enter a word to check the number of vowels in it:")
count=0

for letter in word: #running through each letter in the given word
	if "aeiou":
		count+=1
	else:
		count=count

print("The word", word, "contains", count, "vowels")

#OR

for letter in word: #running through each letter in the given word
	if letter=="a" or letter=="e" or letter=="i" or letter=="o" or letter=="u":
		count+=1
	else:
		count=count

print("The word", word, "contains", count, "vowels")