import random
import time

def worstCase(r):
    return list(range(r, 0, -1))

def bestCase(r):
    return list(range(1, r + 1))

def randomCase(r):
    randArray = list(range(1, r + 1))
    random.shuffle(randArray)
    return randArray

def bubbleSort(array):
    comparisons = 0
    swaps = 0
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(array)-1):
            comparisons += 1
            if array[i] > array[i+1]:
                swaps += 1
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True
    return {'c' : comparisons, 's' : swaps}

def combSort(array):
    comparisons = 0
    swaps = 0
    n = len(array)
    gap = n
    shrink = 1.3
    swapped = True
    while swapped:
        gap = int(gap / shrink)
        if gap == 10 or gap == 9:
            gap = 11
        if gap > 1:
            swapped = True
        else:
            gap = 1
            swapped = False
        i = 0
        while i + gap < n:
            comparisons += 1
            if array[i] > array[i + gap]:
                swaps += 1
                array[i], array[i + gap] = array[i + gap], array[i]
                swapped = True
            i = i + 1
    return {'c' : comparisons, 's' : swaps}
