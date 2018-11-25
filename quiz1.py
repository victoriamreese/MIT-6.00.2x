#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 12:07:46 2018

@author: vicky
"""

# 1.playlist for party
# collection of songs 
#(name (string), song_length (float >= 0), song_size (float >= 0)))
#goal - optimize playlist to play songs for as long as posible without taking up more than 
#max_disk_size


demo_songs = [('bridges', 5.5, 3.0),('cow', 8.0, 10.0),('favorite', 2.7, 3.0),('musho', 4.3, 2), ('banga', 2.3, 4)]

#approach:
# loop through song list - add first song that will fit on the disk to playlist in order of list
# then add songs from smallest to largest size until there is no space



def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    playlist = []
    space_used = 0
    songs_copy = songs.copy()
    if songs[0][2] < max_size:
        playlist.append(songs[0][0])
        space_used += songs[0][2]
        songs_copy.sort(key=lambda tup: tup[2])
        for n in songs_copy:
            if (n[0] not in playlist) and (space_used + n[2] <= max_size):
                playlist.append(n[0])
                space_used += n[2]
    return playlist
        
   
li = [0,1,2,3,4,5,6,7,8]
t1 = [2,4,3,-5,-3,4,7]
#2.find maximum sum of a contiguous subsequence
    
def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    max = []
    for i in range(len(L)):
        for j in range(len(L)+1):
            test = L[i:j]
            if sum(max) < sum(test):
                max = test
    return sum(max)


def f(x):
    if x**2 == 9:
        return True



def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True 
        In case of ties, return any one of them. 
    """
    best = []
    for i in range(-120, 120):
        if test((i)) == True:
            best.append(i)
    return max(best)
            
#problem cases:
#exponenents - should only accept positive answers
#e.g x**2 
