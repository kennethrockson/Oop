# using the input() function
FN = input("Please enter you first name: ",)
LN = input("Please enter you last name: ",)
SNB = input("What is your street number: ",)
SN = input("What is your street name: ",)
PO = input("what is your Apartment or Box number (if applicable): ",)
CY = input("What City: ",)
ST = input("What State: ",)
ZIP = input("What is your Zip Code: ",)

# Store those elements into a tuple.  
address = (FN, LN, SNB, SN, PO, CY, ST, ZIP)

# Using the data stored in the tuple and produce an address. 
print(f"{address[1].title()}, {address[0].title()}")
print(f"{address[2].title()} {address[3].title()}")

# If the user does not enter a PO Box, the line should be excluded from the output
if PO == "":
    pass
else: 
    print(f"{address[4].upper()}")

print(f"{address[5].title()}, {address[6].upper()}, {address[7]}")

