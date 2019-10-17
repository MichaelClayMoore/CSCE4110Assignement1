def quickSort(L, ascending = True):
    quicksorthelp(L, 0, len(L), ascending)

def quicksorthelp(L, low, high, ascending = True):
    result = 0
    if low < high:
        pivot_location, result = Partition(L, low, high, ascending)
        result += quicksorthelp(L, low, pivot_location, ascending)
        result += quicksorthelp(L, pivot_location + 1, high, ascending)
    return result

def modified_quickSort(L, ascending = True):
    modified_quicksorthelp(L, 0, len(L), ascending)

def modified_quicksorthelp(L, low, high, ascending = True):
    result = 0

    if (high - low) < 100:
        insertionSort(L, low, high)

    elif low < high:
        pivot_location, result = Partition(L, low, high, ascending)
        result += modified_quicksorthelp(L, low, pivot_location, ascending)
        result += modified_quicksorthelp(L, pivot_location + 1, high, ascending)
    return result

def median_of_three(L, low, high):
    mid = (low+high-1)//2
    a = L[low]
    b = L[mid]
    c = L[high-1]

    if a <= b <= c:
        return b, mid
    if c <= b <= a:
        return b, mid
    if a <= c <= b:
        return c, high-1
    if b <= c <= a:
        return c, high-1

    return a, low

def Partition(L, low, high, ascending = True):
    result = 0
    pivot, pidx = median_of_three(L, low, high)
    L[low], L[pidx] = L[pidx], L[low]
    i = low + 1
    for j in range(low+1, high, 1):
        result += 1
        if (ascending and L[j] < pivot) or (not ascending and L[j] > pivot):
            L[i], L[j] = L[j], L[i]
            i += 1
    L[low], L[i-1] = L[i-1], L[low]
    return i - 1, result

# this was found on geeks for geeks:
# https://www.geeksforgeeks.org/python-program-for-insertion-sort/
# Function to do insertion sort
def insertionSort(arr, low, high):

    # Traverse through 1 to len(arr)
    for i in range(low, high):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key

def swap(array_given, pos1, pos2):
    array_given[pos1] = array_given[pos1] ^ array_given[pos2]
    array_given[pos2] = array_given[pos1] ^ array_given[pos2]
    array_given[pos1] = array_given[pos1] ^ array_given[pos2]
