#!/usr/bin/env python
# coding: utf-8
#

import copy

def exchange(a, b):
    return b, a

def insert_selection(input_arr):
    arr = copy.deepcopy(input_arr)
    num = len(arr)
    for i in range(num):
        value = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > value:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = value
    return arr

def bubble_sort(input_arr):
    arr = copy.deepcopy(input_arr)
    num = len(arr)
    flag = True
    while flag:
        flag = False
        for i in range(1, num):
            j = num - i
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = exchange(arr[j], arr[j - 1])
                flag = True
    return arr

def selection_sort(input_arr):
    arr = copy.deepcopy(input_arr)
    num = len(arr)
    for i in range(0, num):
        minj = i
        for j in range(i, num):
            if arr[j] < arr[minj]:
                minj = j
            arr[i], arr[minj] = exchange(arr[i], arr[minj])
    return arr
            
if __name__ == '__main__':

    try:
        while True:
            # arr = [2, 3, 1, 5, 4]
            arr = list(map(int, input().strip().split(' ')))
            # print(arr)
            # print(insert_selection(arr))
            # print(bubble_sort(arr))
            print(selection_sort(arr))
    
    except EOFError:
        pass
        
