############################
#####code challenge 26######
############################

# pseudo code 
"""
  InsertionSort(int[] arr)

    FOR i = 1 to arr.length

      int j <-- i - 1
      int temp <-- arr[i]

      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1

      arr[j + 1] <-- temp
"""



# making insertion sort function takes an array and return the array sorted 
def insertion_sort(array):
    """insertion sort""" #list = [8,4,23,42,16,15]
    for i in range (1 , len(array)): # we consider the first element as sorted
        temp = array[i] # pointer is the current element
        # now we start comparing the anchor to the elements before it
        j = i - 1
        while j >= 0 and array[j] > temp:
            array[j+1] = array[j]
            j = j - 1
        array[j+1] = temp
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
    print(insertion_sort(list))



