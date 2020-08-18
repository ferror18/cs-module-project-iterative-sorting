def selection_sort(arr):
    # loop through n-1 elements
    for current in range(len(arr)):
        min_idx = current 
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(current+1, len(arr)): 
            if arr[min_idx] > arr[j]: 
                min_idx = j 
            

        # TO-DO: swap
        # Your code here
        arr[current], arr[min_idx] = arr[min_idx], arr[current] 
    return arr

def mp(arr):
        return len(arr) // 2