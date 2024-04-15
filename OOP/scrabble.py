#Asks the user to enter a word.
word = input("Enter a word: ",).upper()

# The points associated with each letter are shown below:
# a dictionary that maps from letters to point values.
points = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'R': 1, 'S': 1, 'T': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10}

#The program will compute and display the Scrabble score for the word entered by the user. 
sscore = 0
for letter in word:
    sscore += points.get(letter, 0)

#Print to the screen, as an f-string, the word and its score in a user-friendly message    
print(f"Your word '{word}' is worth {sscore} points.")
