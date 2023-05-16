# Has higher space complexity & not a in-place sort algorithm
def quickSort(arr):
    if len(arr)<=1:
        return arr
    
    pivot = arr.pop()

    items_lower = []
    items_higher = []

    for i in arr:
        if i < pivot:
            items_lower.append(i)
        else:
            items_higher.append(i)

    return quickSort(items_lower) + [pivot] + quickSort(items_higher)

arr = [4,7,2,6,0,2]
print(quickSort(arr))