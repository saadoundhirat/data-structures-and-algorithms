# merge Sort

## merge Sort pseudo code

pseudo code for insertion sort:
    ```
    
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
    ```

python code for insertion sort:

```
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
```


## merge Sort visually

- image: to see the image go to static/lab27/merge_Sort

![White Board Image](mergeSOrt.png)

## Miro link

Miro: <https://miro.com/app/board/o9J_l0dN_jE=/>
