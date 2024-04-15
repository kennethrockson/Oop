sum = 0
count = 0

# Program that computes the average of values that are entered by the user. 
while True:

# The user can enter as many numbers as desired.  
    V = input("Enter a number or q to quit: ")
    
# The user will end the program by entering the letter q.
    if V == 'q':
        break
    
    else:
#   The program will print out sum, count, and average of numbers entered
        V = int(V)
        
        sum += (V)
        
        count += 1
        avg = sum / count
   
print("The sum of the numbers enters is",sum)
print("The count of the numbers enters is",count)
if count == 0:
    print("The average of the numbers enter is 0")
else:
    print("The average of the numbers enters is",avg)