# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 14:00:57 2021

@author: Stuart
"""

import time


def partition(data, head, tail, drawData, tickRate):
    # border = head
    # pivot = data[tail]

    # drawData(data, getColorArray(len(data), head, tail, border, border))    

    # for j in range(head, tail):
    #     if data[j] < pivot:
    #         drawData(data, getColorArray(len(data), head, tail, border, j, True)) 
    #         time.sleep(tickRate)
            
    
    #         data[border], data[j] = data[j], data[border]
    #         border += 1
            
    # drawData(data, getColorArray(len(data), head, tail, border, j)) 
    # time.sleep(tickRate)
            

    # #swap pivot with border value
    # drawData(data, getColorArray(len(data), head, tail, border, tail, True)) 
    # time.sleep(tickRate)    
    # data[border], data[tail] = data[tail],data[border]
        
    # return border
    
    pivot = data[head]
    leftwall = head
    drawData(data, getColorArray(len(data), head, tail, leftwall, leftwall))
    time.sleep(tickRate)

    for i in range(head+1, tail):
        if (data[i] < pivot):
            drawData(data, getColorArray(len(data), head, tail, leftwall, i, True))
            time.sleep(tickRate)
            data[i], data[leftwall] = data[leftwall], data[i]
            leftwall = leftwall+1
                
        drawData(data, getColorArray(len(data), head, tail, leftwall, i)) 
        time.sleep(tickRate)
                   
    #swap pivot and leftwall
    pivot, data[leftwall] = data[leftwall], pivot
    
    drawData(data, getColorArray(len(data), head, tail, leftwall, tail, True)) 
    time.sleep(tickRate)  
    
    return leftwall


def quick_sort(data, head, tail, drawData, tickRate):
    
    #quick_sort(data, 0, len(data)-1, drawData, speedScale.get())
   
    if head < tail:
        
        pivot = partition(data, head, tail, drawData, tickRate)
        
        
        #left partition
        quick_sort(data, head, pivot, drawData, tickRate)
        
        #right partition 
        quick_sort(data, pivot+1, tail, drawData, tickRate)
    
    
    
        #this causes it to make all flash green when finishing each pass for a given pivot- fix!
        drawData(data, ['green' for x in range(len((data)))])   
    
    
    
def getColorArray(dataLen, head, tail, leftwall, currentIndex, isSwapping = False):
    
    colorArray = []
    for i in range(dataLen):
        #base colour
        if i >= head and i<= tail:
            colorArray.append('light blue')   #partition working on
        else: 
            colorArray.append('gray')  #partition not working on 
        
        if i == tail: 
            colorArray[i] = 'purple'      #
            
        elif i == leftwall: 
            colorArray[i] = 'red'   #
            
        elif i == currentIndex: 
            colorArray[i] = 'yellow'     #currentIndex being checked
            
        if isSwapping:
            if i == leftwall or i == currentIndex: 
                colorArray[i] = 'green'     #if swapping the two elements
                
    return colorArray