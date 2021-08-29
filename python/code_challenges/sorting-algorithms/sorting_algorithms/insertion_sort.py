############################
#####code challenge 26######
############################

# making insertion sort function takes an array and return the array sorted 

def insertion_sort(array):
    """insertion sort"""









# def insertion_sort(array):
#     for i in range(1, len(array)):
#         j = i
#         while j > 0 and array[j] < array[j-1]:
#             array[j], array[j-1] = array[j-1], array[j]
#             j -= 1
#     return array

# def insertion_sort(arr):
    # """insertion sort function"""
#     for i in range(1, len(arr)):
#         j = i-1
#         key = arr[i]
#         while (arr[j] > key) and (j >= 0):
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = key
#     return arr


if __name__ == "__main__":
    list = [8,4,23,42,16,15]
    #Reverse-sorted: 
    list1 = [20,18,12,8,5,-2]
    #Few uniques:
    list2 = [5,12,7,5,5,7]
    #Nearly-sorted: 
    list3 = [2,3,5,7,13,11]

    print(insertion_sort(list))



