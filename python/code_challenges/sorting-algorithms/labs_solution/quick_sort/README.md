# Challenge Summary
<!-- Description of the challenge -->
Write a function that implements the quick sort algorithm
the function takes a list and start of the lest and the end of the list and return the list sorted

- Note:  Im using Hoare schema partition to do the quick sort

## Whiteboard Process
<!-- Embedded whiteboard image -->

![White Board Image](visual_merge.png)

## Miro link

Miro: <https://miro.com/app/board/o9J_l0dN_jE=/>

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
- to sort an array has n elements in descending order using quick sort algorithm
- first we found the write index for the pivot where there will be two partitions
- after we have the partitions and index of the pivot we can use that to use recurion to repeat the process and keep doing that until  the start of the array is greater than the end of the array

## Solution
<!-- Show how to run your code, and examples of it in action -->
"""
    poetry install
    poetry run python quick_sort.py
"""