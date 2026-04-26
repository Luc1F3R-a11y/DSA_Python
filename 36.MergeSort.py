def mergeSort(arr):
    n = len(arr)
    if n <=1:
        return arr
    
    mid = n // 2
    left = arr[:mid]
    right =arr[mid:]

    return merge(left, right)
    
def merge(left, right):
    result =[]
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result
