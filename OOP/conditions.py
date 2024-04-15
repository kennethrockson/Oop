# Created 3 variables
letter1 = "m"

letter2 = "u"

letter3 = "y"

vowels = "aeiou"

#testing the first variable set with if-elif-else statements w/ f-strings
if letter1 in vowels:
    print(f"{letter1} is a vowel")

elif letter1 == "y":
    print(f"{letter1} is a y")
    
else:
    print(f"{letter1} is a consonant") 

#testing the second variable set with if-elif-else statements w/ f-strings
if letter2 in vowels:
    print(f"{letter2} is a vowel")

elif letter2 == "y":
    print(f"{letter2} is a y")
    
else:
    print(f"{letter2} is a consonant")
    
#testing the third variable set with if-elif-else statements w/ f-strings    
if letter3 in vowels:
    print(f"{letter3} is a vowel")

elif letter3 == "y":
    print(f"{letter3} is a y")
    
else:
    print(f"{letter3} is a consonant")

#output prints statements for all variables