###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = {}

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    allTrips = []
    cowsCopy = cows.copy()
    cowsSorted = sorted(cowsCopy.items(), key=lambda x: x[1], reverse = True)
    while sum(cowsCopy.values()) > 0:
        ship = []
        total = 0
        for cow, value in cowsSorted:
            if cowsCopy[cow] != 0 and value + total <= limit:
                ship.append(cow)
                total += value
                cowsCopy[cow] = 0
        allTrips.append(ship)
    return allTrips
#                

            
            #elif # cow is too heavy
            # keep in list
            


# as is now, this code prints only one possible combination with betsy and only betsy.


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # creates all options using get partitions, labels each "train"
    # checks if sum of all values in the car within the train are less than the total
    # sets the key as the len for determining the minimum
    return min([train for train in get_partitions(cows)
                if all(sum(cows[c] for c in car) <= limit for car in train)
             ], key = len)
    
    
#    cowsCopy = cows.copy()
#    alltotals=[]
#    print(cowsCopy)
#    for combination in get_partitions(cowsCopy):
#        for trip in combination:
#            triptotal = 0
#            for cow in trip:
#                triptotal += cowsCopy[cow]
#            alltotals.append(triptotal) #alltotals now contains all weights of cows in one 
#        for number in alltotals:
#            if number >= limit:
#                pass
#            else:
#                return combination
#            
            

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=10
#print(cows)

#print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))



# greedy algorithm
# must sort the weights of our items
# sorted items (big to small)
# start with biggest item
# loop through remaining
# if adding an item will cause the totalweight to be too high, stop and close out that list
# all possibilities, we must start with smaller and smaller items..
# we are not choosing which solution is better, we are simply generating all the possible solutions. 

