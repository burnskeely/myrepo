sentence=input("Please enter a sentence: ")

newsentence=""

for letter in sentence:
	if letter==" " or letter=="!" or letter=="." or letter=="," or letter=="?":
		newsentence = newsentence
	else:
		newsentence=newsentence+letter

print("Your new sentence is", newsentence)