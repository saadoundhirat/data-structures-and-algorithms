def quick_sort(elements , start , end):
    """quick sort Algorithm"""
    # using the "Hoare" schema 
    # first put the pivot in the right position so we can have partition 
    if start < end:
        pi = partition(elements , start, end)
        # after we have the pivot index we do the recursive part for left partition and right partition
        quick_sort(elements, start, pi-1) # left partition
        quick_sort(elements, pi+1, end) # right partition

def partition(elements ,start ,end):
    """to make the pivot in the right position and return the pivot_index"""
    # make the pointers 
    pivot_index = start
    pivot = elements[pivot_index]

    # first to move the start element and compare it to the pivot value 
    while start < end :
        # we have to make sure that start is in range of the array len
        while start < len(elements) and elements[start] <= pivot:
            start += 1
        while end > 0 and  elements[end] > pivot:
            end -= 1  
        # at this point we stop the start point and the right pointer then we swap them 
        if start < end:
            swap(start ,end ,elements)

        # after this we swap the end with the pivot 
    swap(pivot_index , end , elements)

    # now the end value is the pivot so we return the end 
    return end
    
def swap(a, b, arr):
    if a!=b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp

if __name__ == "__main__":
    elements = [11,9,29,7,2,15,28]
    print(elements)
    quick_sort(elements ,0 , len(elements)-1)
    print(elements)