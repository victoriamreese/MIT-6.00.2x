#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 22:09:09 2018

@author: vicky
"""
#first attempt
def yieldAllCombosOne(items):
    """
        Generates all combinations of N items into two bags, whereby each 
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list 
        of which item(s) are in each bag.
    """
    N = len(items)
    for i in range(8):
# this loop was created to visualize binary shift
        for j in range(3):
            print(i, "in binary is", bin(i)[2:].zfill(3))
            print("i = ", i, " j = ", j)
            print(i, ">>", j, ":", "the answer is", i >> j)
            print("in binary, that equals:", bin(i >> j)[2:].zfill(3))
            



#second attempt
#pretty close the first time. why do you need 3**j
def yieldAllCombosTwo(items):
    N = len(items)
    for i in range(3**N):
        print(i)
        bag1 = []
        bag2 = []
        for j in range(N):
            print((i // (3 ** j)) % 3)
            if (i // (3 ** j)) % 3 == 1: 
                bag1.append(items[j])
            elif (i // (3 ** j)) % 3 == 0:
                bag2.append(items[j])            
        yield (bag1, bag2)


yieldAllCombosTwo(['chicken', 'pie', 'photo'])


#Greedy algorithm example:
def greedy(items, maxCost, keyfunction):
    """Assumes items a list, maxCost >= 0,
    keyFunction maps elements of items to numbers"""
    itemsCopy = sorted(items, key = keyFunction, reverse = True) #sorted takes 3 args, 1) iterable to be sorted, 2) key - basis of comparison 3) reverse, arrangement of sorting 
    result = [] # initialize empty list for result
    totalValue, totalCost = 0.0, 0.0 # initialize value and cost to 0
    for i in range(len(itemsCopy)): #iterate through as amny times as there are items. 
        if (totalCost+itemsCopy[i].getCost()) <= maxCost:# if the current accrued cost plus the cost of the item under consideration at iteration i is less than the max cost,
            result.append(itemsCopy[i]) # this item will be added to the results
            totalCost += itemsCopy[i].getCost() #the cost of the item is added to total cost
            totalValue += itemsCopy[i].getValue() # the value of the item is added to total cost
    return (result, totalValue)


#lambda expressions - anonymous functions
    # only use these when the function you wish to wrtie is very short
#example lambdas
f1 = lambda x: x # spits x back out
f2 = lambda x, y: x+y #
f3 = lambda x, y: 'factor' if (x%y == 0) else 'not factor'

# be creative - what other cool functions might you use lambda for?
f4 = lambda x, y: (x**2 + 2*x*y + y**2)
f5 = lambda string, times: ('Hello, you wanted me to say ' + str(string) + '. ')* times



#Brute Force algorithm example - recursive
# enumerate all possible combination of items
# eliminate those that violate constraints
def maxVal(toConsider, avail):
    """Assumes toConsider a list of items, avail a weithg
    Returns a tuple of the total value of a solution to a 0/1 knapsack problem and the items of that solution """
    if toConsider == [] or avail == 0: # first checks if there are no mor values in toconsider or if avail is 0
        result = (0, ())
    elif toConsider[0].getUnits() > avail: #checks if first element of toConsider is greater than avail
        result = maxVal(toConsider[1:], avail) # if yes, maxVal function runs again without first element
    else: #if first element is smaller than the availabe space, we work with it
        nextItem = toConsider[0] # make the first element of toConsider "next item"
        withval, withToTake = maxVal(toConsider[1:], avail - nextItem.getUnits()) #run maxVal again without first term and subtract value from available 
        withVal += nextItem.getValue() #this represents the value of the items you took 
        withoutVal, withoutToTake = maxVal(toConsider[1:], avail) 
    if withVal > withoutVal:
        result = (withVal, withToTake + (nextItem,))
    else:
        result = (withoutVal, withoutToTake)
    return result



# we can improve or specify more constraints on our algorithm
    #reminder - tinker tinekr tinker 


# Recursive Fibonacci -
# brute force algorithm with unacceptable values omitted is 2^8 complexity, which isn't that big
# dynamic programming can help us speed up these very complex algorithms 

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
#how does this function work?
        # well, the base case is n=0 or n=1 
        so lets say we want th 