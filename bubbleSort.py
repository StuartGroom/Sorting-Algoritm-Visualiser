# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 13:35:16 2021

@author: Stuart
"""

import time

def bubble_sort(data, drawData, tickRate):
    
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                
                drawData(data, ['green' if x == j+1 else 'light blue' for x in range(len(data))])
                time.sleep(tickRate)
    drawData(data, ['green' for x in range(len(data))])

