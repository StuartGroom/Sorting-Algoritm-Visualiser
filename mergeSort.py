# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 14:57:55 2021

@author: Stuart
"""

import time 

def merge_sort(data, drawData, tickRate):
    
    merge_sort_algo(data,0, len(data)-1, drawData, tickRate)
    
    
    
def merge_sort_algo(data, left, right, drawData, tickRate):
    
    if left < right: 
        middle = (left+right) // 2 
        
        #split left side recursively 
        merge_sort_algo(data, left, middle, drawData, tickRate)
        #split right side recursively 
        merge_sort_algo(data, middle+1, right, drawData, tickRate)
        
        merge(data, left, middle, right, drawData, tickRate)

    
def merge(data, left, middle, right, drawData, tickRate) :
    
    drawData(data, getColorArray(len(data), left, middle,right))
    time.sleep(tickRate)
    
    leftPartition = data[left:middle+1] #gets all elements from left 50% of array
    
    rightPartition = data[middle+1:right+1] #gets all elements from right 50% of array
    
    leftIndex = rightIndex = 0 #initialise indices
    
    for dataIndex in range (left, right+1): #dataIndex points to main array, start from left and go to right
        if leftIndex < len(leftPartition) and rightIndex < len(rightPartition): #check if both indices are in their partition
            if leftPartition[leftIndex] <= rightPartition[rightIndex]:  
                data[dataIndex] = leftPartition[leftIndex]     
                leftIndex += 1
            else:   
                data[dataIndex] = rightPartition[rightIndex]
                rightIndex += 1
        
        elif leftIndex < len(leftPartition): #if left index is still in the left partition
             data[dataIndex] = leftPartition[leftIndex]
             leftIndex +=1 
        else: 
            data[dataIndex] = rightPartition[rightIndex]
            rightIndex +=1 
             
    drawData(data, ['green' if x >= left and x <= right else 'light blue' for x in range(len(data))])
    time.sleep(tickRate)
            
        
def getColorArray(length, left, middle, right):
    colorArray = []
    
    for i in range(length):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                colorArray.append('yellow')
            else: 
                colorArray.append('pink')
        else: 
            colorArray.append('light blue')
    
    return colorArray
                        
                                  
    
    
    
    
    