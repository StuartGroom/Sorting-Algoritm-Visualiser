# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 12:04:44 2021

can have issues with tkinter window not responding, then suddenly gets updated as finished
-due to calcs for algorithm + tkinket being on same thread and tkinter is paused to complete calc processed

@author: Stuart
"""

from tkinter import *
from tkinter import ttk
import tkinter as tk 

import webbrowser

import random
from bubbleSort import bubble_sort
from quickSort import quick_sort 
from mergeSort import merge_sort 
from radixSort import radix_sort 
from insertionSort import insertion_sort


#!/usr/bin/env python
import psutil
# gives a single float value
psutil.cpu_percent()
# gives an object with many fields
psutil.virtual_memory()
# you can convert that object to a dictionary 
dict(psutil.virtual_memory()._asdict())


#set main window 
root = Tk()
root.title('Sorting Algorithm Visualisor')
root.maxsize(900,600)
root.config(bg='black')


#variables
selectedAlgo = StringVar()
data = [] 

def Generate():
    global data
    
    minVal = int(minScale.get()) #fetch string minEntry and convert to int
    maxVal = int(maxScale.get())
    sizeVal = int(sizeScale.get())

    
    data = []
    
    for _ in range(sizeVal):
        if minVal == maxVal:
            data.append(minVal)
        else: 
            data.append(random.randrange(minVal, maxVal+1)) #maxVal + 1 as randrange isnt max inclusive
    
    drawData(data, ['light blue' for x in range(len(data))]) #pass in array of red for all elements in array
    
    
    
def startAlgo():
    
    global data
    if not data: return #if no data in data array
    
    if (algMenu.get() == 'Bubble sort'):
    
        bubble_sort(data, drawData, speedScale.get())
    
    elif (algMenu.get() == 'Quick sort'):
        
        quick_sort(data, 0, len(data), drawData, speedScale.get())
        
    elif (algMenu.get() == 'Merge sort'):
        
        merge_sort(data, drawData, speedScale.get())

    elif (algMenu.get() == 'Radix sort'):
        
        radix_sort(data, drawData, speedScale.get())
        
    elif (algMenu.get() == 'Insertion sort'):
        insertion_sort(data, drawData, speedScale.get())

def drawData(data, colorArray):
    canvas.delete("all") # clears canvas each time generate button is pressed
    c_height = 380
    c_width = 770 #10 less than actual canvas size as to leave 10p on each side (done on left by offset below)
    #width of bars for graph- calculated as can have different number of data points
    x_width = c_width / (len(data) + 1)
    offset = 10 #so graph doesnt start at border
    
    
    normalizedData = [i/max(data) for i in data]
    
    for i, height in enumerate(normalizedData):
        #top left
        x0 = i * x_width + offset 
        y0 = c_height - height * 340 #times by 340 so max value will be almost as tall as the canvas height
        #bottom right 
        x1 = (i + 1) * x_width + offset
        y1 = c_height 
        
        
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        
        if sizeScale.get() <= 50:    #write number over bar if less than 50 data entries
            canvas.create_text(x0+5, y0-10, text=str(data[i])) #write number over bar

    root.update_idletasks()


def onClick(x): #opens youtube video on the topic
    webbrowser.open(x,new=1)
    
def infoPopUp():
    
    headerFont= ("Verdana 12 underline")
    bodyFont = ("Helvetica", 10)
    # def leavemini():
    #     popup.destroy()
        
    if (algMenu.get() == 'Bubble sort'):
       
        popup = tk.Tk()
        popup.wm_title("Bubble sort")
        popup.minsize(400, 400)
        popup.maxsize(800, 800)
        
        header = ttk.Label(popup, text="Bubble Sort Explained", font= headerFont, anchor="center")
        header.pack(side="top", fill="x", pady=10)
        
        body = ttk.Label(popup, text= bubbleSortText(), font= bodyFont, wraplength=700, justify="center", anchor="center")
        body.pack(side="top", fill="x", pady=10)
        
        footer = ttk.Label(popup, text= bubbleSortComplexity(), font= bodyFont, wraplength=700, justify="center", anchor="center")
        footer.pack(side="top", fill="x", pady=10)
        
        url = "https://www.youtube.com/watch?v=xli_FI7CuzA"
        B1 = ttk.Button(popup, text="learn more", command=lambda: onClick(url))
        B1.pack()
        


    elif (algMenu.get() == 'Quick sort'):
        
        popup = tk.Tk()
        popup.wm_title("Quick sort")
        popup.minsize(400, 400)
        popup.maxsize(800, 800)
        
        header = ttk.Label(popup, text="Quick Sort Explained", font= headerFont, anchor="center")
        header.pack(side="top", fill="x", pady=10)
        
        body = ttk.Label(popup, text= quickSortText(), font= bodyFont, wraplength=700, justify="center", anchor="center")
        body.pack(side="top", fill="x", pady=10)
        
        footer = ttk.Label(popup, text= quickSortComplexity(), font= bodyFont, wraplength=700, justify="center", anchor="center")
        footer.pack(side="top", fill="x", pady=10)
        
        url = "https://www.youtube.com/watch?v=Hoixgm4-P4M"
        B1 = ttk.Button(popup, text="learn more", command=lambda: onClick(url))
        B1.pack()
        
        
        
        
    elif (algMenu.get() == 'Merge sort'):
        
        popup = tk.Tk()
        popup.wm_title("Merge sort")
        popup.minsize(400, 400)
        popup.maxsize(800, 800)
       
        header = ttk.Label(popup, text="Merge Sort Explained", font= headerFont, anchor="center")
        header.pack(side="top", fill="x", pady=10)
        
        body = ttk.Label(popup, text= mergeSortText(), font= bodyFont, wraplength=700, justify="center",anchor="center")
        body.pack(side="top", fill="x", pady=10)
        
        footer = ttk.Label(popup, text= mergeSortComplexity(), font= bodyFont, wraplength=700, justify="center", anchor="center")
        footer.pack(side="top", fill="x", pady=10)
        
        url = "https://www.youtube.com/watch?v=4VqmGXwpLqc"
        B1 = ttk.Button(popup, text="learn more", command=lambda: onClick(url))
        B1.pack()
        
       

    elif (algMenu.get() == 'Radix sort'):
        
        popup = tk.Tk()
        popup.wm_title("Radix sort")
        popup.minsize(400, 400)
        popup.maxsize(800, 800)
        
        header = ttk.Label(popup, text="Radix Sort Explained", font= headerFont, anchor="center")
        header.pack(side="top", fill="x", pady=10)
        
        body = ttk.Label(popup, text= radixSortText(), font= bodyFont, wraplength=700, justify="center", anchor="center")
        body.pack(side="top", fill="x", pady=10)
        
        footer = ttk.Label(popup, text= radixSortComplexity(), font= bodyFont, wraplength=700, justify="center", anchor="center")
        footer.pack(side="top", fill="x", pady=10)
        
        url = "https://www.youtube.com/watch?v=XiuSW_mEn7g&t=90s"
        B1 = ttk.Button(popup, text="learn more", command=lambda: onClick(url))
        B1.pack()
        
    elif (algMenu.get() == 'Insertion sort'):
        
        popup = tk.Tk()
        popup.wm_title("Insertion sort")
        popup.minsize(400, 400)
        popup.maxsize(800, 800)
        
        header = ttk.Label(popup, text="Insertion Sort Explained", font= headerFont, anchor="center")
        header.pack(side="top", fill="x", pady=10)
        
        body = ttk.Label(popup, text= insertionSortText(), font= bodyFont, wraplength=700, justify="center", anchor="center")
        body.pack(side="top", fill="x", pady=10)
        
        footer = ttk.Label(popup, text= insertionSortComplexity(), font= bodyFont, wraplength=700, justify="center", anchor="center")
        footer.pack(side="top", fill="x", pady=10)
        
        url = "https://www.youtube.com/watch?v=JU767SDMDvA"
        B1 = ttk.Button(popup, text="learn more", command=lambda: onClick(url))
        B1.pack()
        
    
    
    popup.mainloop()

def bubbleSortText() :
    
    return("Sort by comparing each adjacent pair of items in a list in turn, swapping the items if necessary, and repeating the pass through the list until no swaps are done.")

def quickSortText() :
    
    return("Quick Sort is a sorting algorithm, which is commonly used in computer science. Quick Sort is a divide and conquer algorithm. It creates two empty arrays to hold elements less than the pivot value and elements greater than the pivot value, and then recursively sort the sub arrays.")

def mergeSortText() :
    
    return("Merge Sort is a sorting algorithm, which is commonly used in computer science. Merge Sort is a divide and conquer algorithm. It works by recursively breaking down a problem into two or more sub-problems of the same or related type, until these become simple enough to be solved directly. The solutions to the sub-problems are then combined to give a solution to the original problem. So Merge Sort first divides the array into equal halves and then combines them in a sorted manner.")

def radixSortText() :
    
    return("Radix sort is an integer sorting algorithm that sorts data with integer keys by grouping the keys by individual digits that share the same significant position and value (place value).")
    
def insertionSortText():
    
    return("An insertion sort compares values in turn, starting with the second value in the list. If this value is greater than the value to the left of it, no changes are made. Otherwise this value is repeatedly moved left until it meets a value that is less than it. The sort process then starts again with the next value.")




def bubbleSortComplexity() :

    return("Complexity of Bubble Sort.\n\nTime Complexity:\nWorst Case: O(n^2)\nAverage Case: Θ(n^2)\nBest Case: Ω(n)\n\nSpace Complexity:\nO(1)\n\nWhere n is the number of items being sorted.")    

def quickSortComplexity() :
    
    return("Complexity of Quick Sort.\n\nTime Complexity:\nWorst Case: O(n^2)\nAverage Case: Θ(n log(n))\nBest Case: Ω(n log(n))\n\nSpace Complexity:\nO(log(n))\n\nWhere n is the number of items being sorted.")    

    
def mergeSortComplexity() :

    return("Complexity of Merge Sort.\n\nTime Complexity:\nWorst Case: O(n log(n))\nAverage Case: Θ(n log(n))\nBest Case: Ω(n log(n))\n\nSpace Complexity:\nO(n)\n\nWhere n is the number of items being sorted.")    
 

def radixSortComplexity() :
    
    return("Complexity of Merge Sort.\n\nTime Complexity:\nWorst Case: O(nk)\nAverage Case: Θ(nk)\nBest Case: Ω(nk)\n\nSpace Complexity:\nO(n+k)\n\nWhere n is the number of items being sorted and k is the number of digits in the largest number.")    
 
def insertionSortComplexity() :
    
    return("Complexity of Insertion Sort.\n\nTime Complexity:\nWorst Case: O(n^2)\nAverage Case: Θ(n^2)\nBest Case: Ω(n)\n\nSpace Complexity:\nO(1)\n\nWhere n is the number of items being sorted.")    
 
    

#top UI for settings 
UI_frame = Frame(root, width=600, height=200, bg='grey')
UI_frame.grid(row=0, column=0, padx= 10, pady =5)


#bottom for visualisation
canvas = Canvas(root, width=780, height= 380, bg='white')
canvas.grid(row=2, column=0, padx=10, pady=5)



#User Interface Area
#row[0]
    #combobox for selecting which algo to use
Label(UI_frame, text="Algorithm: ", bg='gray').grid(row=0, column=0, padx=5, pady =5, sticky=W)
algMenu = ttk.Combobox(UI_frame, values=['Bubble sort', 'Quick sort', 'Merge sort', 'Radix sort', 'Insertion sort'], textvariable=selectedAlgo)
algMenu.grid(row=0, column=0, padx=70, pady=5)

Button(UI_frame, text="Info on Algorithm", command= infoPopUp, bg='white' ).grid(row=0, column=1, padx= 5, pady=5 )

    
speedScale = Scale(UI_frame, from_=0, to=0.5, length = 200, digits=2, resolution= 0.1, orient= HORIZONTAL, label="Select Tickrate (Seconds)")
speedScale.grid(row=0, column=2, padx= 5, pady=5)

#button to call the generate fucn. 
Button(UI_frame, text="Start", command=startAlgo, bg='red' ).grid(row=0, column=3, padx= 5, pady=5 )


#row[1]
sizeScale = Scale(UI_frame, from_=3, to=200, length = 200, digits=1, resolution= 0.2, orient= HORIZONTAL, label="Sample Size")
sizeScale.grid(row=1, column=0, padx= 5, pady=5)


minScale = Scale(UI_frame, from_=1, to=10, length = 200, digits=1, resolution= 1, orient= HORIZONTAL, label="Minimum Value")
minScale.grid(row=1, column=1, padx= 5, pady=5)


maxScale = Scale(UI_frame, from_=10, to=50, length = 200, digits=1, resolution= 1, orient= HORIZONTAL, label="Maximum Value")
maxScale.grid(row=1, column=2, padx= 5, pady=5)

#button to call the generate fucn. 
Button(UI_frame, text="Generate", command=Generate, bg='white' ).grid(row=1, column=3, padx= 5, pady=5 )



root.mainloop()



