from helpers import *
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i


    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    r = len(arr)-1
    l = 0
    while l <= r: 
  
        mid = l + (r - l) // 2; 
          
        # Check if x is present at mid 
        if arr[mid] == target: 
            return mid 
  
        # If x is greater, ignore left half 
        elif arr[mid] < target: 
            l = mid + 1
  
        # If x is smaller, ignore right half 
        else: 
            r = mid - 1
            
    return -1  # not found
