############################
#####code challenge 27######
############################

"""

ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
       # sort the left side
      Mergesort(left)
       # sort the right side
      Mergesort(right)
       # merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
"""



# making insertion sort function takes an array and return the array sorted 
def merge_sort(array):
    """merge sort""" 
    n = len(array)
    if n > 1:
        mid = n // 2
        left = array[:mid]
        right = array[mid:]
        merge_sort(left)
        merge_sort(right)
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    return array
    

if __name__ == "__main__":
    list = [8,4,23,42,16,15]
    #Reverse-sorted: 
    list1 = [20,18,12,8,5,-2]
    #Few uniques:
    list2 = [5,12,7,5,5,7]
    #Nearly-sorted: 
    list3 = [2,3,5,7,13,11]

    #unordered:
    print(list)
    #Sorted:
    print(merge_sort(list))



