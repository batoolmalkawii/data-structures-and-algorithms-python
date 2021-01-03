def insertion_sort(input_list):
    for i in range (1, len(input_list)):
        j = i - 1
        temp = input_list[i]

        while j >= 0 and temp < input_list[j]:
            input_list[j+1] = input_list[j]
            j = j - 1
        
        input_list[j+1] = temp

    return (input_list)

if __name__ == "__main__":
    print(insertion_sort([8,4,23,42,16,15]))


            


    