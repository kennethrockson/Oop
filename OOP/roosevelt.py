# Taking the phrase and convert it to a list
quote = "The only thing we have to fear is fear itself"
quote_list = quote.split()

# Create a new empty list
newlist = []

# Inspect each word in the list
for word in quote_list:
    first_letter = word[0].lower()
# If the word in the list starts with a vowel add the letters "way" to the end of the word by using append
    if first_letter in 'aeiou':
        newlist.append(word + "way")
# If the word in the list does not start with a vowel
# the first letter from the word and move it to the end and append
    else:
        newlist.append(word[1:] + first_letter + "ay")

# convert the new list to a string and print that string out         
new_sentence = " ".join(newlist)
print(new_sentence)
        
        
        