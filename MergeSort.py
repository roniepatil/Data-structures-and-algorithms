def MergeSort(arr):
    if len(arr) > 1:

        mid = len(arr)//2
        subarray1 = arr[:mid]
        subarray2 = arr[mid:]


        MergeSort(subarray1)
        MergeSort(subarray2)

        i = j = k =0

        while i < len(subarray1) and j < len(subarray2):
            if subarray1[i] < subarray2[j]:
                arr[k] = subarray1[i]
                i += 1
            else:
                arr[k] = subarray2[j]
                j += 1
            k += 1


        while i < len(subarray1):
            arr[k] = subarray1[i]
            i+=1
            k+=1
        
        while j < len(subarray2):
            arr[k] = subarray2[j]
            j+=1
            k+=1


arr = [10,9,2,4,6]
MergeSort(arr)
print(arr)