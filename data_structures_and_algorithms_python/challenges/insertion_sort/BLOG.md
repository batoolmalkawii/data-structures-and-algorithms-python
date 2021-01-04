# Insertion  Sort

Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. 
It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

## Problem Domain:
Write a function that implements the Insertion sort algorithm, where the input is a list and the output is the sorted list.

## Algorithm
To sort an array of size n in ascending order:

    1: Iterate from arr[1] to arr[n] over the array.

    2: Compare the current element (key) to its predecessor.

    3: If the key element is smaller than its predecessor, compare it to the elements before. Move the greater elements one position up to make space for the swapped element.

## Pseudo Code:
```
InsertionSort(int[] arr)
  
    FOR i = 1 to arr.length
    
      int j <-- i - 1
      int temp <-- arr[i]
      
      WHILE j >= 0 AND temp < arr[j]
        arr[j + 1] <-- arr[j]
        j <-- j - 1
        
      arr[j + 1] <-- temp
```

## Trace (Visual):
#### Input: [8,4,23,42,16,15]
**Step 1**: 8 and 4 are compared, 4 is less than 8, they are swapped.
![](../../../assets/insertion_sort/Slide1.PNG)
**Step 2**: 8 and 23 are compared, 23 is greater than 8, they are not swapped.
![](../../../assets/insertion_sort/Slide2.jpg)
**Step 3**: 23 and 42 are compared, 42 is greater than 23, they are not swapped.
![](../../../assets/insertion_sort/Slide3.jpg)
**Step 4**: 42 and 16 are compared, 16 is less than 42, they are swapped.
![](../../../assets/insertion_sort/Slide4.PNG)
**Step 5**: 23 and 16 are compared, 16 is greater than 23, they are swapped.
![](../../../assets/insertion_sort/Slide5.PNG)
**Step 6**: 8 and 16 are compared, 16 is greater than 8, they are not swapped.
![](../../../assets/insertion_sort/Slide6.jpg)
**Step 7**: 42 and 15 are compared, 15 is less than 42, they are swapped.
![](../../../assets/insertion_sort/Slide7.PNG)
**Step 8**: 23 and 15 are compared, 15 is less than 8, they are swapped.
![](../../../assets/insertion_sort/Slide8.PNG)
**Step 9**: 16 and 15 are compared, 15 is less than 16, they are swapped.
![](../../../assets/insertion_sort/Slide9.PNG)
**Step 10**: 8 and 15 are compared, 15 is greater than 8, they are not swapped.
![](../../../assets/insertion_sort/Slide10.jpg)
**Step 11**: The list is sorted>
![](../../../assets/insertion_sort/Slide11.jpg)


## Time Complexity:
Best Case:
* If A is sorted: `O(n)` comparisons.

Worst Case
* If A is reversed sorted: `O(n^2)` comparisons.

Average Case
* If A is randomly sorted: `O(n^2)` comparisons.


## Space Complexity:
* Since the insertion algorithm sorts elements in the
input array, this algorithm is sorts elements in-place,
which means it does not need additional memory
space other than the input array size.
* Therefore, it requires `n` elements space, which means
it is efficient in terms of memory space.


## Advantages and Disadvantages:
Advantages:
* Efficient in terms of time if the input array is
already sorted (best-case scenario).
* Efficient in terms of memory space (in-place).
* Easy to design - only two nested loops.

Disadvantages:
* Not efficient in terms of running time (worst-case
and average-case scenarios).

