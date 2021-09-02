

def quick_sort(elements , start , end):
    """quick sort Algorithm"""
    if len(elements) <= 1:
        return elements

    if start < end:
        pi = partition(elements , start, end)
        quick_sort(elements, start, pi-1) # left partition
        quick_sort(elements, pi+1, end) # right partition
    # for test
    return elements

def partition(elements ,start ,end):
    """to make the pivot in the right position and return the pivot_index"""
    pivot_index = start
    pivot = elements[pivot_index]
    while start < end :
        while start < len(elements) and elements[start] <= pivot:
            start += 1
        while end >= 0 and elements[end] > pivot:
            end -= 1  
        if start < end:
            swap(start ,end ,elements)
    swap(pivot_index , end , elements)
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

    a = [2, 1, 3, 4, 5, 6, 7, 8, 9, 10]
    quick_sort(a, 0, len(a)-1)
    print(a)

    print(quick_sort([5,4,3,2,1], 0, len([5,4,3,2,1])-1))