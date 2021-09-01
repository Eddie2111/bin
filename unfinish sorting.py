import random,time;
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


main = []

def readFile():
    with open('c:/Users/Edward Zephyr/Desktop/nothing/Assignment/cse221/test1.txt','r') as textico:
        a = textico.readline()
    a = a.split(',')
    a=[int(i) for i in a] 
    return a

def array_generation(x=8):
    if len(main)!=0:
        return main
    else:
        while len(main)!=x:
            g = random.randint(1,20)
            if g not in main:
                main.append(g)
    return main

def bubbleSort(arr):   
    for i in range(len(arr)): 
        swap=False
        for j in range(0,len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j+1],arr[j]=arr[j],arr[j+1]
                swap=True
                print(arr)
        if not swap:break;

def selectionSort(a): #not recursive
    g = []
    indexingLength = range(0,len(a)-1)
    for i in indexingLength:
        min_value = i
        for j in range(i+1,len(a)):
            if a[j]<a[min_value]:
                min_value=j
                #print(a)
        if min_value != i:
            a[min_value],a[i]=a[i],a[min_value]
            print(a)
    print(a)
    return a

def insertion_sort(array):
    for index in range(1, len(array)):
        currentValue = array[index]
        currentPosition = index
        while currentPosition > 0 and array[currentPosition - 1] > currentValue:
            array[currentPosition] = array[currentPosition -1]
            currentPosition = currentPosition - 1
        array[currentPosition] = currentValue
        print(array)
############################ quick sort #########################

def partition(arr, low, high):
	i = (low-1)
	pivot = arr[high]
	for j in range(low, high):
		if arr[j] <= pivot:
			i = i+1
			arr[i], arr[j] = arr[j], arr[i]
			print(arr)
	arr[i+1], arr[high] = arr[high], arr[i+1]
	return (i+1)

def quickSort(arr, low, high):
	if len(arr) == 1:
		return arr
	if low < high:
		pi = partition(arr, low, high)
		print(arr)
		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1, high)
#################################################################

def mergeSort(array,size):
    if len(array) > 1:
        r = len(array)//2
        L = array[:r]; M = array[r:];
        mergeSort(L,size); mergeSort(M,size);
        i = j = k = 0
        if len(array)==size:
            print(array)
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
                if len(array)==size: print(array);
            else:
                array[k] = M[j]
                j += 1
            k += 1
            if len(array)==size: print(array);
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
            if len(array)==size:
                print(array)
        while j < len(M):
            array[k] = M[j]
            j += 1; k += 1;
            if len(array)==size: print(array);
def output():
    print( ' = ' * 24)
    a = readFile()
    print ('Initial Array → ',a)
    print ('Bubble Sort')
    bubbleSort(a)
    time.sleep(1)
    print( ' = ' * 24)
    a = readFile()
    print ('Initial Array → ',a)
    print(' Selection Sort ')
    selectionSort(a)
    time.sleep(1)
    print( ' = ' * 24)
    a = readFile()
    print ('Initial Array → ',a)
    print (' Insertion Sort ')
    insertion_sort(a)
    time.sleep(1)
    print( ' = ' * 24)
    a = readFile()
    print ('Initial Array → ',a)
    print ( 'Quick Sort ' )
    quickSort(a,0,len(a)-1)
    time.sleep(1)
    print( ' = ' * 24)
    a = readFile()
    print ('Initial Array → ',a)
    print (' Merge Sort ')
    mergeSort(a,len(a))
    time.sleep(1)
    print( ' = ' * 24)


plt.style.use ('fivethirtyeight')

x = []
y = []
index = count()


plt.tight_layout()
#plt.show()
output()
