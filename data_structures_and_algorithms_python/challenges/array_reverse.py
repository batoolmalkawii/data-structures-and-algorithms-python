def reverseArray(arr):
    new_arr = []
    for element in arr:
        new_arr.insert(0, element)
    return(new_arr)


if __name__ == "__main__":
    arr = [2, 4, 6, 8, 10]
    print(reverseArray(arr))

