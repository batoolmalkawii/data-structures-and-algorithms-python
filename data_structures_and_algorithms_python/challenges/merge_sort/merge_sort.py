def merge_sort(input_list):

    if len(input_list) > 1:
        mid = len(input_list)//2
        left = input_list[:mid]
        right = input_list[mid:]

        merge_sort(left)
        merge_sort(right)
 
        i = j = k = 0
 
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                input_list[k] = left[i]
                i += 1
            else:
                input_list[k] = right[j]
                j += 1
            k += 1
 
        while i < len(left):
            input_list[k] = left[i]
            i += 1
            k += 1
 
        while j < len(right):
            input_list[k] = right[j]
            j += 1
            k += 1
            
    return input_list


if __name__ == "__main__":
    print (merge_sort([8,4,23,42,16,15]))
 