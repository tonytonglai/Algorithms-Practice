# helper function to find the index of the smallest element
def findSmallestInd(arr, index):
    smallest = arr[index]
    smallest_index = index
    for i in range(index, len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


# since it's a sorting algorithm, you only need to take an array as a param
def selectionSort(arr):
    # selection sort works conceptually by getting the smallest/largest item, and then
    # just incrementing array afterwards
    for i in range(len(arr)):
        # assignment of variable
        temp_index = findSmallestInd(arr, i)
        # copy to temp
        temp_value = arr[temp_index]
        arr[temp_index] = arr[i]
        arr[i] = temp_value
    return arr


array1 = [9, 7, 1, 3, 5]
# print(findSmallest(array1))
print(selectionSort(array1))

# for i in range(len(array1)):
#     print(array1[i])
