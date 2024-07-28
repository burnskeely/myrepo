######################
## Python Module
## For Loop
######################

# Count Vowels
word=input("Enter a word:")

count=0
for letter in word:
    if letter.lower() in "aeiou":
        count+=1
print("Count of vowels is:",count)


# Remove Spaces
sentence=input("Enter a sentence:")
newSentence=""

for letter in sentence:
    if letter != " ":
        newSentence = newSentence + letter
print(newSentence)

# Replace Vowels
word=input("Enter a word:")
newWord=""
for letter in word:
    if letter.lower() in "aeiou":
        newWord=newWord+"_"
    else:
        newWord=newWord+letter
print(newWord)

# Insert Asterisk
word=input("Enter a word:")
newWord=""

for letter in word:
    newWord=newWord + letter 
    if letter.lower() in "aeiou":
        newWord=newWord + "*"
print(newWord)