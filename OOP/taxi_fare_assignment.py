#a function named fare_caculator
def fare_caculator(distance):
"""
This function computes the overall taxi fare by taking into account the distance traveled in kilometers.
"""

    #base fare
    basef = 4.00
    #plus $0.25 for every 140 meters traveled
    Farep = 0.25 / (140 / 1000)
    #total distance from fare
    distancef = distance * Farep
    ## Total fare
    total_fare = basef + distancef
    #  formatted as a floating value with two-decimal precision and a 
    floatf = f"${total_fare:.2f}"  # Format the fare
    
    return floatf
#Example 1
print(fare_caculator(3.352))
#Example 2
print(fare_caculator(0))
