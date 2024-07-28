##################################
## Task 5 - Count Vowels    
##################################

# 1-	Add a new file: CountVowels.py and make it the startup file  
# 2-	Inputs a word (a string)
# 3-	Counts how many vowels are in the word   
# Tip: You can scroll through every character of a string using its index.
#	 For example, if word =  'hello' then word[0] is the letter h and word[1] is the letter e.
#	 Use the len() function to find the length of a string. For example, in the above example, len(word) is 5.
#	 Use simple if statement/s to detect if the character is 'a', 'e', 'i', 'o'  or  'u'
#	 Every time you find a vowel you must increase a counter (an integer variable)
#
#	In the next chapter (Lists) you'll discover a much easier way of performing this task.

word=input("Enter a word:")
length=len(word)
vowels="aeiou"

i=0
counter=0
while (i < length):
    if word[i] in "aeoiu":
        counter=counter+1
    i+=1

print("number of vowels in ",word, " = ", counter)