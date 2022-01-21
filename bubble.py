# bubble sort compares the first element with the element beside it.
# if the value of the first element is larger than the second, the elements will swap positions.
# iteration will continue until the array is sorted.

arr = [5, 3, 8, 2, 4, 1, 9, 7, 6]

arr2 = [22, 56, -93, 43, 27, 32]


def bubblesort(arr):

    for i in range(len(arr)):
        var = i
        for j in range(i+1, len(arr)):

            # compare first element with the one beside it
            if arr[var] > arr[j]:

                # swap positions if the first element is larger
                arr[i], arr[j] = arr[j], arr[i]

    # print("Sorted array: ")
    return arr


# test 1
print("Unsorted array: ")
print(arr)
print("Sorted array: ")
print(bubblesort(arr))

# test 2
print("\nUnsorted array: ")
print(arr2)
print("Sorted array: ")
print(bubblesort(arr2))
