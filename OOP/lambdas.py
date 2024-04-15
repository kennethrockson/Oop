# Taking a list of employee names
names_list=['Frank Harrelson', 'Bob Sharles', 'Bob Tranklin', 'Bob Grody', 'Hank Charles', 'Bob Rarrelson', 
'Mack Slobson', 'John Jonones', 'Rob Wranklin', 'Tom Simpsonian', 'Rob Rearrelson', 'John Moodys', 
'Frank Shones', 'John Harrelson','Frank Quhorles', 'Tom Pharles', 'Frank Fwanklin', 'Frank Charleston', 
'John Arles', 'John Georanklin', 'Frank Dobsonsoson', 'Diane Johnston', 'Dob Scone', 'Michael Scarn', 
'Goldie Hawn', 'Billie Holliday', 'Woody Harrelson', 'Arthur Rubinstein', 'Thomas Edison', 'Robert Goulet']
# Sort the list by their last name
names_list.sort(key=lambda name:name.split()[-1].lower())
# Print out the sorted names list on the screen.
print(names_list)

# New list of user names based on the first 5 characters of their last name and the first 2 characters of their first name
new_list = []

#Use one of the lambda expressions discussed to create the "five and two" user names.
new_list = list(map(lambda name:name.split()[0][:5] + name.split()[1][:2], names_list))

#Print out the new list on the screen.
print(new_list)
