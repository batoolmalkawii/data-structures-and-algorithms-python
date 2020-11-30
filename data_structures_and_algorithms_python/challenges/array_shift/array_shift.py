import math

def insertShiftArray(arr, val):
    if arr == []:
        return([val])
    if len(arr) == 1:
        arr.append(val)
        return(arr)
    new_arr = []
    middle_index = math.ceil(len(arr)/2)
    i = 0
    while i < len(arr):
        if i == middle_index:
            new_arr.append(val)
            new_arr.append(arr[i])
        else:
            new_arr.append(arr[i])
        i += 1

    return(new_arr)

def removeShiftArray(arr):
    if arr == [] or len(arr) == 1:
        return([])
    new_arr = []
    middle_index = math.floor(len(arr)/2)
    i = 0
    while i < len(arr):
        if i != middle_index:
            new_arr.append(arr[i])
        i += 1
    
    return (new_arr)
   


if __name__ == "__main__":
    print(insertShiftArray([2,4,6,8], 5))
    print(insertShiftArray([4,8,15,23,42], 16))
    print(removeShiftArray([2,4,6,8]))
    print(removeShiftArray([4,8,15,23,42]))
    print(insertShiftArray([2], 4))

