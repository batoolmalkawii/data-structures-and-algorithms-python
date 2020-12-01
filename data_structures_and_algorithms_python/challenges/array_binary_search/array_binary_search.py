import math

def binarySearch(arr, key):
    start = 0
    end = len(arr) - 1
    middle = 0

    while (start <= end):
        middle = (start + end) // 2
        if key > arr[middle]:
            start = middle + 1
        elif key < arr[middle]:
            end = middle - 1
        else:
            return middle
    return -1

if __name__ == "__main__":
    print(binarySearch([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21], 19))