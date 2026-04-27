def quickSort(arr, low, high):
    if low < high:
        pivot_idx = partition(arr, low, high)
        quickSort(arr, low, pivot_idx - 1)
        quickSort(arr, pivot_idx + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1