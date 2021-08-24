# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 16:03:50 2021

@author: Stuart
"""

import time
from functools import reduce

def radix_sort(data, drawData, tickRate):
    
    num_digits = get_num_digits(data)
    data = radix_sort_algo(data, num_digits, drawData, tickRate)
    
    drawData(data, ['green' for x in range(len(data))])
    time.sleep(tickRate)
    
    return data

def get_num_digits(data):
    
    _max = 0
    for item in data:
        _max = max(item, _max)
    
    return len(str(_max)) #gets how many characters are in the str version of number


def radix_sort_algo(data, num_digits, drawData, tickRate):


    for digit in range(0, num_digits):
        
        
        B = [[] for i in range(10)] #2d list with 10 empty buckets
        for item in data:
           
            
            num = item // 10 ** (digit) % 10 
            B[num].append(item) #appends item into correct bucket
            
            
            drawData(data, getColorArray(data, len(data), num))
            time.sleep(tickRate)
        
            data = flatten(B)   
            
            
    return data
        
def flatten(data):
    
    return reduce(lambda x,y: x + y, data)
    

def getColorArray(data, dataLen, bucket):
    
    colorArray = []
    # secondRun = False
    
    # for i in range(dataLen):
            
    #     if (int(str(data[i])[0]) >= 5) : 
            
    #         secondRun = True 
            
    # if secondRun == True: #if its in first of 2 digits
         
    for i in range(dataLen):    
        # if (len(str(data[i])) == 1) : #if this number is single digit
        #     num = "0" #first digit is set to 1 as default
        # else:
            # num = str(data[i])[1]
            
        if (len(str(data[i])) == 1):
            num = str(data[i])
        else: 
            num = str(data[i])[1]
            
        print(num)    
        if num == "0":
            colorArray.append('red')
            
        elif num == "1":
            colorArray.append('orange')
            
        elif num == "2":
            colorArray.append('yellow')
            
        elif num == "3":
            colorArray.append('green')
            
        elif num == "4":
            colorArray.append('blue')
            
        elif num == "5":
            colorArray.append('indigo')
            
        elif num == "6":
            colorArray.append('violet')
        
        elif num == "7":
            colorArray.append('black')
            
        elif num == "8":
            colorArray.append('white')
            
        elif num == "9":
            colorArray.append('silver')
                
        
    # else:   #2nd run so all single digits
    #     for i in range(dataLen):    
            
    #         if (len(str(data[i])) == 1):
    #             num = "0" #first digit is set to 1 as default
    #         else:
    #             num = str(data[i])[1]
                
    #         if num == "0":
    #             colorArray.append('red')
                
    #         elif num == "1":
    #             colorArray.append('orange')
                
    #         elif num == "2":
    #             colorArray.append('yellow')
                
    #         elif num == "3":
    #             colorArray.append('green')
                
    #         elif num == "4":
    #             colorArray.append('blue')
                
    #         elif num == "5":
    #             colorArray.append('indigo')
                
                 
                
    
        
   
    return colorArray

