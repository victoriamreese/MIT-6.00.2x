#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 12:26:27 2018

@author: vicky
"""

#Simulations - much more practical when done in programs, not by hand
#Location, Field, Drunk
#how far will a drunk actor get after a certain number of steps?

#Structure of Simulation:
#simulate one walk of k steps
#simulate n such walks
#report average distance from origin

#useful abstractions:
# alwyas a good idea to create abstractions for things you will use many times

class Field(object):
    def __init__(self):
        self.drunks = {}
    
    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc
        
    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]
    
    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        #use move method of Locatino to get new location
        self.drunks[drunk] = currentLocation.move(xDist, yDist)

#this class is a base class to be inheritied. all children will have names
class Drunk(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'This drunk is named " + self.name

    
import random

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0, 1.0), (0.0, -1.0), (1.0, 0,0), (-1.0, 0.0)]
        return random.choice(stepChoices)
    
class ColdDrunk(Drunk):
    def takeStep(self):
        [(0.0,0.9),(0.0,-1.1),(1.0,0.0),(-1.0,0.0)]
    return random.choice(stepChoices)

class Location(object):
    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y
    
    def move(self, deltaX, deltaY):
        """deltaX and deltaY are floats"""
        return Location(self.x + deltaX, self.y + deltaY)
    
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5 #use pythagorean theorem
    def __str__(self):
        return '<' + str(self.x) + ';' + str(self.y) + '>'
    

def walk(f, d, numSteps):
    """Assumes: f a Field, d a drunk in f, and numSteps an int >= 0.
       Moves d numSteps times; returns the distance between the final location and the location at the start of the walk."""
       start = f.getLoc(d)
       for s in range(numSteps):
           f.moveDrunk(d)
       return start.distFrom(f.getLoc(d))
   
def simWalks(numSteps, numTirals, dClass):
    """Assumes numSteps an int >= 0, numTrials an int >0, dClass a subclass of Drunk Simulates numTrials walks of numSteps steps each. returns a list of the final distances for each trial."""
    Homer = dClass()
    origin = Location(0,0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)
        distances.append(round(walk(f, Homer, numTrials), 1))
    return distances

#test 
def drunkTest(walkLengths, numTrials, dClass):
    """Assumes walkLengths a sequence of ints >= 0 numTrials an int > 0, dClass a subclass of Drunk For each number of steps in walkLength, runs simWalks with numTrials walks and prints results """
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dClass)
        print(dClass.__name__, 'random walk of', numSteps, 'steps')
        print(' Mean =', round(sum(distances)/len(distances), 4))
        print(' Max =', max(distances), 'Min =', min(distances))