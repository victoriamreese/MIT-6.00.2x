#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 10:40:42 2018

@author: vicky
"""

#visualizing data using existing libraries
import pylab as plt # this allows us to access any module in pylab with plt.<modulename>

#generate random example data

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []


for i in range (0,30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i) # usually use 2 but 1.5 will fit better on this plot
    
plt.clf()
plt.figure('big')    # creates a new plot that includes the following  
plt.plot(mySamples, myCubic)
plt.plot(mySamples, myQuadratic)
plt.xlabel('sample points')
plt.ylabel('test subjects')
plt.title('YUM!!!')
plt.ylim(0,1000)
plt.figure('small')
plt.plot(mySamples, myLinear)


#example function
# this is awesome! I can wrtie a function like this for my savings and financial picture tracking!

def retire(monthly, rate, terms):
    savings = [0]
    base = [0]
    mRate = rate/12
    for i in range(terms):
        base+= [i]
        savings += [savings[-1]*(1+mRate)+monthly]
    return base, savings

def displayRetireMonthlies(monthlies, rate, terms):
    plt.figure('retireMonth')
    plt.clf() #this makes it reusable, fram will clear each time function is run. 
    for monthly in monthlies:
        xvals, yvals = retire(monthly, rate, terms)
        plt.plot(xvals, yvals, label = 'retire:' + str(monthly))
        plt.legend(loc = 'upper right')
        
        
def displayRetireWRates(month, rates, terms):
    plt.figure('retireRate')
    plt.clf()
    for rate in rates:
        xvals, yvals = retire(month, rate, terms)
        plt.plot(xvals, yvals, label = 'retire:' + str(month)+ ':' + \
                 str(int(rate*100)))
        plt.legend(loc = 'upper left')
        
    
        
displayRetireMonthlies([500, 600, 700, 800, 900, 1000, 1100], .05, 40*12)
displayRetireWRates(800,[.03, .05, .07], 40*12)