#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 23:27:43 2018

@author: vicky
"""

# review probability
#inferential statistics
#roulette 

import random

class FairRoulette():
    def __init__(self):
        self.pockets = []
        for i in range(1,37):
            self.pocekts.append(i)
        self.ball = None
        self.blackOdds, self.redOdds = 1.0, 1.0
    def spin(self):
        self.ball = random.choice(self.pockets)
    def isBlack(self):
        if type(self.ball) != int:
            return False
        if ((self.ball > 0 and self.ball <= 10)
            or (self.ball > 18 and self.ball <= 28)):
            return self.ball%2 == 0
        else:
            return self.ball%2 == 1
    def isRed(self):
        return type(self.ball) == int and not self.isBlack()
    def betBlack(self, amt):
        if self.isBlack():
            return amt*self.blackOdds
        else:
            return -amt
    def betRed(self, amt):
        if self.isRed():
            return amt*self.redOdds
        else:
            return -amt*self.redOdds
    def betPocket(self, pocket, amt):
        if str(pocket) == str(self.ball):
            return amt*self.pocketOdds
        else:
            return -amt
    def __str__(self):
        return 'Fair Roulette'
    

def playRoulette(game, numSpins, toPrint = True):
    luckyNumber = '2'
    bet=1
    totRed, totBlack, totPocket = 0.0, 0.0, 0.0
    for i in range(numSpins):
        game.spin()
        totRed += game.betRed(bet)
        totBlack += game.betBlack(bet)
        totPocket += game.betPocket(luckyNumber, bet)
    if toPrint:
        print(numSpins, 'spins of', game)
        print('Expected return betting red= ', str(100*totRed/numSpins) + '%')
        print('Expected return betting black= ', str(100*totBlack/numSpins) + '%')
        print('Expected return betting', luckyNumber, '=', str(100*totPocket/numSpins) + '%\n')
    return (totRed/numSpins, totBlack/numSpins, totPocket/numSpins)
        

#types of roulette
    
class EuRoulette(FairRoulette):
    def __init__(self):
        FairRoulette.__init__(self)
        self.pockets.append('0')
    def __str__(self):
        return 'European Roulette'

class AmRoulette(EuRoulette):
    def __init__(self):
        EuRoulette.__init__(self)
        self.pockets.append('00')
    def __str__(self):
        return 'American Roulette'
    
def findPocketReturn(game, numTrials, trialSize, toPrint):
    pocketReturns = []
    for t in range(numTrials):
        trialVals = playRoulette(game, trialSize, toPrint)
        pocketReturns.append(trialVals[2])
    return pocketReturns
    

def stdDevOfLengths(L):
    import math
    #calculate mean
    sums = 0
    diffsquared = []
    for str in L:
        sums += len(str)
    mean = sums / len(L)
    #calc devs squared
    for str in L:
        diffsquared.append((len(str) - mean)**2)
    sumsquares = (sum(diffsquared))
    print(math.sqrt(sumsquares/len(L)))
    
        

#tests:
    
L1=['mango', 'poop', 'cows']



stdDevOfLengths(L1)
    
        
#checking the empirical rule

import scipy.integrate

def gaussian(x, mu, sigma):
    factor1= (1.0/(sigma*((2*pylab.pi)**0.5)))
    factor2 = pylab.e**-(((x-mu)**2)/(2*sigma**2))
    return factor1*factor2

def checkEmpirical(numTrials):
    for t in range(numTrials):
        mu = random.randint(-10,10)
        sigma = random.randint(1,10)
        print('For mu =', mu, 'and sigma =', sigma)
        for numStd in (1, 1.96, 3):
            area = scipy.integrate.quad(gaussian, mu-numStd*sigma, mu+numStd*sigma, (mu, sigma))[0]
            print('Fraction within', numStd, 'std =', round(area, 4))
            
            
#Central limit theory: given a sufficiently large sample, the means of the samples in a set of samples will result in an approximately normal cure normal cruve
            # the mean of the means of the sample will be roughtly the same as the mean of teh population
            #the variance of teh sample means will be roughly that of the means of the population
# die with random real number 0-5, continuous
# code to check CLT:
def plotMeans(numDice, numRolls, numBins, legend, color, style):
    means = []
    for i in range(numRolls//numDice):
        vals = 0
        for j in range(numDice):
            vals += 5*random.random()
        means.append(vals/float(numDice))
    pylab.hist(means, numBins, color = color, label = legend, weights = pylab.array(len(means)*[1])/len(means), hatch = style)
    return getMeanAndStd(means)


        

####################
## Helper functions#
####################
def flipCoin(numFlips):
    '''
    Returns the result of numFlips coin flips of a biased coin.

    numFlips (int): the number of times to flip the coin.

    returns: a list of length numFlips, where values are either 1 or 0,
    with 1 indicating Heads and 0 indicating Tails.
    '''
    with open('coin_flips.txt','r') as f:
        all_flips = f.read()
    flips = random.sample(all_flips, numFlips)
    return [int(flip == 'H') for flip in flips]


def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

    
#############################
## CLT Hands-on             #
##                          #
## Fill in the missing code #
## Do not use numpy/pylab   #
#############################
meanOfMeans, stdOfMeans = [], []
sampleSizes = range(10, 500, 50)

def clt():
    """ Flips a coin to generate a sample. 
        Modifies meanOfMeans and stdOfMeans defined before the function
        to get the means and stddevs based on the sample means. 
        Does not return anything """
    for sampleSize in sampleSizes:
        sampleMeans = []
        for t in range(20):
            sample = flipCoin(sampleSize) # flipCoin returns 1 and 0,
            sampleMeans.append(getMeanAndStd(sample)[0])
        meanOfMeans.append(getMeanAndStd(sampleMeans)[0])
        stdOfMeans.append(getMeanAndStd(sampleMeans[1]))
        
#finding pi with buffon-laplace:
def throwNeedles(numNeedles):
    inCircle = 0
    for Needles in range(1, numNeedles+1, 1):
        x = random.random()
        y = random.random()
        if (x*x + y*y)**0.5 <= 1.0:
            inCircle += 1
    return 4*(inCircle/float(numNeedles))

#this calculates ratio of needles in to out of circle
    
def getEst(numNeedles, numTrials):
    estimates = []
    for t in range(numTrials):
        piGuess = throwNeedles(numNeedles)
        estimates.append(piGuess)
    sDev = stdDev(estimates)
    curEst = sum(estimates)/len(estimates)
    print('Est. = ' + str(curEst) + ', Std. dev. = '  + str(round(sDev, 6)) + ', Needles = ' + str(numNeedles))
    return (curEst, sDev)


def estPi(precision, numTrials):
    numNeedles = 1000
    sDev = precision
    while sDev >= precision/2:
        curEst, sDev = getEst(numNeedles, numTrials)
        numNeedles *= 2
    return curEst 

#general use of monte carlo - needles in / in + out of area 
    # pcik and enclising region, E such that the area of E is easy to calculate and R lies completely within E
    # pikc a set of random points that lie within E
    # let F be the fraction of the points that fall within R
    # multiply the area of E by F
    
  
#e.g. monte carlo function that gives probability of 3 of same color marble in a row
def oneTrial():    
    balls = ['r', 'r', 'r', 'g', 'g', 'g']
    chosenBalls = []
    for t in range(3):
        ball = random.choice(balls)
        balls.remove(ball)
        chosenBalls.append(ball)
    if chosenBalls[0] == chosenBalls[1] == chosenBalls[2]:
        return True
    return False
    

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    numTrue = 0
    for trial in range(numTrials):
        if oneTrial():
            numTrue += 1
    return float(numTrue)/float(numTrials)
    


#probability sampling: each member of a population as a nonzero probability of being included in a sample
#simple random sampling : each member has an equal chance of being chosen. 
    # this is not always appropriate
    #e.g. in sitauions in which there is a majority group and minority subgroups, smaple is subdivided into subgroups to avoid over sampling of majority group
    
    
    
#example 
def makeHist(data, title, xlabel, ylabel, bins = 20):
    pylab.hist(data, bins=bins)
    pylab.title(title)
    pylab.xlabel(xlabel)
    pylab.ylabel(ylabel)

def getHighs():
    inFiles = open('temperatures.csv')
    populaton = []
    for l in inFiles:
        try:
            tempC = float(l.split(','[1]))
            population.append(tempC)
        except:
            continue
    return population

def getMeansAndSDs(population, sample, verbose = False):
    popMean = sum(population)/len(population)
    sampleMean = sum(sample)/len(sample)
    if verbose:
        makeHist(population, 'Daily High 1961-2015, Population\n' +\ 
                 '(mean = ' + str(round(popMean, 2)) + ')', 'Degrees C', 'Number Days')
        pylab.figure()
        makeHist(sample, 'Daily High 1961-2015, Sample\n' +\
             '(mean = ' + str(round(popMean, 2)) + ')', 'Degrees C', 'Number Days')
        print('Population mean =', popMean)
        print('Standard deviation of population =', numpy.std(population))
        print('Sample mean=' sampleMean)
        print('Standard devaiton of sample =',
          numpy.std(sample))
return popMean, sampleMean, \
numpy.std(population), numpy.std(sample)

random.seed(0)
population = getHighs()
sample = random.sample(population, 100)
getMeanAndSDs(population, sample, True)

    