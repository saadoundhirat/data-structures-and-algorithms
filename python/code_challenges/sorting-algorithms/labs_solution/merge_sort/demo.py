############################
#####code challenge 27######
############################
# making insertion sort function takes an array and return the array sorted 
# def merge_sort(array):
#     """merge sort""" 
#     n = len(array)
#     if n > 1:
#         mid = n // 2
#         left = array[:mid]
#         right = array[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i, j, k = 0, 0, 0
#         while i < len(left) and j < len(right):
#             if left[i] <= right[j]:
#                 array[k] = left[i]
#                 i += 1
#             else:
#                 array[k] = right[j]
#                 j += 1
#             k += 1
#         while i < len(left):
#             array[k] = left[i]
#             i += 1
#             k += 1
#         while j < len(right):
#             array[k] = right[j]
#             j += 1
#             k += 1
#     return array

# this is recursive function, this works but take more space
# def merge_sort_sol(array):
#     # if length of the list <= 1 then return list
#     if len(array) <= 1:
#         return array

#     mid = len(array)//2

#     left = array[:mid]
#     right = array[mid:]

#     left = merge_sort_sol(left)
#     right = merge_sort_sol(right)
        
#     return merge_two_sorted_array(left , right)


# def merge_two_sorted_array(a, b):
#     """merge two sorted array"""
#     result = []
#     i= j =0
#     while i < len(a) and j < len(b):
#         if a[i] <= b[j]:
#             result.append(a[i])
#             i += 1
#         else:
#             result.append(b[j])
#             j += 1

#     while i < len(a):
#         result.append(a[i])
#         i += 1

#     while j < len(b):
#         result.append(b[j])
#         j += 1

#     return result

def merge_sort_sol(array):
    # if length of the list <= 1 then return list
    if len(array) <= 1:
        return array

    mid = len(array)//2
    left = array[:mid]
    right = array[mid:]

    merge_sort_sol(left)
    merge_sort_sol(right)

    merge_two_sorted_array(left , right , array)

    return array

def merge_two_sorted_array(a, b ,array):
    """merge two sorted array"""
    i= j =k =0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            array[k] = a[i]
            i += 1
        else:
            array[k] = b[j]
            j += 1
        k += 1

    while i < len(a):
        array[k] = a[i]
        i += 1
        k += 1

    while j < len(b):
        array[k] = b[j]
        j += 1
        k += 1




if __name__ == "__main__":
    # list = [8,4,23,42,16,15]
    # #Reverse-sorted: 
    # list1 = [20,18,12,8,5,-2]
    # #Few uniques:
    # list2 = [5,12,7,5,5,7]
    # #Nearly-sorted: 
    # list3 = [2,3,5,7,13,11]

    # #unordered:
    # print(list)
    # #Sorted:
    # print(merge_sort(list))
    # list_one= [4,8,12,16]
    # list_two= [7,11,32,256]
    # print(merge_two_sorted_array(list_one ,list_two))

    # try_list = [0,-1,54,62,-30,97,80,46]
    # print(merge_sort_sol(try_list))


    try_list = [0,-1,54,62,-30,97,80,46]
    print(merge_sort_sol(try_list))