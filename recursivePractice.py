def sum(arr, total):
    # base case, array is empty
    if len(arr) == 0:
        return total

    # recursive case; there is somethin in the array
    total += int(arr.pop(0))
    # you MUST return the recursive function in python
    return sum(arr, total)

arr1 = [2,4,6]
print(sum(arr1, 0))