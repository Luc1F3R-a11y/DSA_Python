def countingSort(arr):
    if len(arr) == 0:
        return arr
    
    max_val = max(arr)
    min_val = min(arr)
    range_val = max_val - min_val + 1
    
    count = [0] * range_val
    output = [0] * len(arr)
    
    for i in arr:
        count[i - min_val] += 1
    
    for i in range(1, range_val):
        count[i] += count[i-1]
    
    for i in range(len(arr)-1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1
    
    return output