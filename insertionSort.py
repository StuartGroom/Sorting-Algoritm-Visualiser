# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 15:35:18 2021

@author: Stuart
"""

import time

def insertion_sort(data, drawData, tickRate):
    
    for index in range(1, len(data)): #range starts from 2nd item (nothing to left of first item to compare to)
        
        value = data[index]
        indexS = index

        while data[index-1] > value and index>0:   #loop until you reach first item of list
            
            # drawData(data, ['green' if x == j+1 else 'red' for x in range(len(data))])
            # time.sleep(tickRate)
            
            drawData(data, getColorArray(len(data), index, indexS))
            time.sleep(tickRate)
            
            
            # drawData(data, ['green' if x == index else 'gray' for x in range(len(data))])
            # time.sleep(tickRate)
                
            data[index], data[index-1] = data[index-1], data[index]
            index = index- 1 #decrement i 
           
        drawData(data, ['green' for x in range(len(data))])
    return data
     


def getColorArray(dataLen, index, indexS):
     
    colorArray = []
     
    for i in range(dataLen):
         
        if i == index: 
             colorArray.append('red')
        elif i < indexS: 
             colorArray.append('green')
        else:
             colorArray.append('light blue')

    return colorArray



# def getColorArray(dataLen, index):
    
#     colorArray = []
#     for i in range(dataLen):
        
#         if i == index :
#             colorArray[i] = 'blue'
#         elif i == index-1:
#             colorArray[i] = 'red'
      
#     return colorArray




# f i == tail: 
#             colorArray[i] = 'blue'      #
            
#         elif i == leftwall: 
#             colorArray[i] = 'red'   #
            
            


    
    # for _ in range(len(data)-1):
    #     for j in range(len(data)-1):
    #         if data[j] > data[j+1]:
    #             data[j], data[j+1] = data[j+1], data[j]
                
    #             drawData(data, ['green' if x == j+1 else 'red' for x in range(len(data))])
    #             time.sleep(tickRate)
    # drawData(data, ['green' for x in range(len(data))])
    
    