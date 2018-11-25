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
        # adds together numbers one and two less than number entered
        
 #using dynamic programming, we create an empty dictionary to store values previously generated       
def fastFib(n, memo = {}):
    if n ==0 or n ==1:
        return 1
    try:
        return memo[n]
    except KeyError: # KeyError is error when key doesn't exist within a dictionary
        result =  fib(n-1, memo) + fib(n-2, memo)
        memo[n] = result
    return result
        

#Graph Theory
    #general node class

class Node(object):
    def __init__(self, name):
        """Assumes name is a string """
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
    
class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str_(self):
        return self.src.getName() + '->'\
            + self.dest.getName()
   
#common representations of graphs
        # adjacency matrix - rows, source nodes. columns, destination nodes
            # Cells[s, d] = 1 if there is an edge from s to d #0 otherwise
        #adjacency list- associate with each node a list of destination nodes. 
class Digraph(object):
    """edges is a dict mapping each node to a list of its children"""
    def __init__(self):
        self.edges = {}
    
    def addNode(self, node): # a lot of error checking code in this class - that's a good thing!
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []
        
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges and dst in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)

    def childrenOf(self, node):
        return self.edges[node]
    
    def hasNode(self, node):
        return node in self.edges
    
    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)
        
    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = restult + src.getName() + '->'\
                         + dest.getName() + '\n'
        return result[:-1] # omit final new line

class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEgde(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self,rev)
#substitution rule
#sub and super class relationships - 
        # if client code works correctly using an instance of the supertype, 
        # it should also work correctly when an instance of the subtype is substituted for the instance of the supertype
        # in the case of graph and digraph, any progam that works with a digraph will also work with a graph, but
        #but not any program that works with a graph will work with a digraph
        #thus, digraph must be teh supertype and graph is the subtype - seems counterintuitive



#Depth frirst search (DFS) 
        #chooses one child of a node, then the child afer that, until it reaches a deep child node
        #we keep track of the nodes visit to avoid getting caught in a cycle.
        
def DFS(graph, start, end, path, shortest):
    path = path+[start] #path is initialized to be orig path + start path
    if start == end: # if there is only one node, the path is just that node. 
        return path 
    for node in graph.childrenOf(start): #graph is value to be made into graph, childrenOf prints all edges stored as values to the start node 
        if node not in path: #avoid cycles, if we've already gone thru a node, we don't go again
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph, node, end, path, shortest, toPrint) #continues making paths of different lengths, temporaly storing as newpath, then 
                if newPath != None:
                    shortest = newPath
    return shortest
#wrapper function - provides appropriate level of abstraction
def shortestPath(graph, start, end):
    return DFS(graph, start, end, [], None)

#Breadth first search
def BFS(graph, start, end, torPrint = False):
    initPath = [start]
    pathQueue = [initPath]
    if toPrit:
        print('Current BFS path:', printPath(pathQueue))
    while len(pathQueue) != 0:
        #Get and remove oldest element in pathQueue
        tmpPath - pathQueue.pop(0)
        print('Current BFS path:', printPath(tmpPath))
        lastNode = tmpPath[-1]
        if lastNost == end:
            return tmpPath
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not in tmpPath:
                newPath - tmpPath + [nextNode]
                pathQueue.append(newPath)
    return None


                
# I don't think i really understand error throwing and custom exceptions, so I should practice a bit
class testErrorThrow(object):
    def __init__(self):
        self.
        
        try:
            x + y 
        except: 
            