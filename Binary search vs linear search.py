def linearSearch(array, value): # O(n)
    size = len(array) # I dont want to call function len() every iteration so iam going to call it once and store the size in a variable.

    for i in range(0,size): # O(n)
        if array[i] == value:
            return "Found"
    return "Not found"
#------------------------------------------------------------------------------
def binarySearch(array, start, end, value): # O(log(n))
    while(start<=end): # O(log(n))
        mid = int(start + (end - start) / 2)  # (start+end)/2 might cause overflow

        if array[mid] == value:
            return "Found"
        elif array[mid] > value:
            end = mid - 1
        else:
            start = mid + 1

    return "Not found"
