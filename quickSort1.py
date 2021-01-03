# my own implementation of quicksort
def quicksort(arr, low, high):
    # what should my base case be?
    # it should be anything where we've segmented the array into the base case of an array of length 1
    # remember, quicksort needs a PIVOT
    # how would i think of this? perhaps it's mirroring q/p. qp. kewpie. kewpie mayo.

    if len(arr) < 2:
        return arr

    # left hand side + right hand side
    else:
        pivot = arr[low]  # let's just define the pivot as the first value for now (assuming unsorted)
        counter = 1
        for i in range(low,high):
            print(i)
            print("This is low: " + str(low))
            print("This is high: " + str(high))
            if arr[i] <= pivot:
                # swap pivot with element
                counter += 1
                tempVal = arr[i]
                arr[i] = pivot
                pivot = tempVal

        # we now are yielded our new pivot values...

        print("I exited the for loop")
        #quicksorting left-hand side...
        return quicksort(arr, low, pivot - 1)

        #quicksorting right-hand side...
        return quicksort(arr, pivot + 1, high)

arr1 = [3, 5, 2, 1, 4, 7, 6]
print(quicksort(arr1, 0, len(arr1)))

