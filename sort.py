def selectionSort(arr):
    for i in range (9): # loop through array indexes [0-9] and minimum position will be the i index every loop
                        # starts from 0 after one iteration it will be filled, then index 1 will be the minimum
                        # this makes it sequential in the array
        minpos = i 
        for j in range(i, 10): # to search for the minimum value then assign its index to minposition variable
            if arr[j] < arr[minpos]: 
                minpos = j 

        # this code below switches the array value from the one initially in the index we declared min position, 
        # with the one we found to be minimum value. 
        # the loop will search for the minimum value to the right, not including the values in
        # the previous iterations, which were the minimum values found prior.
        temp = arr[i] 
        arr[i] = arr[minpos] # assign the minimim value in min position
        arr[minpos] = temp # put the replaced value in the initial index of minimum value

        print(arr)

def bubbleSort(arr):
    for i in range(len(arr) - 1, 0, -1) : # loop until array is sequential
        for j in range(i):
            if arr[j] > arr[j + 1]: # if value is greater than the number beside it
                temp = arr[j] # swap the values 
                arr[j] = arr[j+1]
                arr[j+1] = temp
        
        print(arr)

def insertionSort(arr):
    for i in range (1, len(arr)): # starting from index one to the length of array
        j = i
        while arr[j - 1] > arr[j] and j > 0: # if left value is bigger than current
            arr[j - 1], arr[j] = arr[j], arr[j-1] # swap
            j -= 1 # go further to the left

            print(arr)

def mergeSort(arr):
    if len(arr) > 1:
        leftArr = arr[:len(arr)//2] # left array is sliced from start of array to midpoint
        rightArr = arr[len(arr)//2:] # right array is sliced from mid point to end

        # loop recursively
        mergeSort(leftArr)
        mergeSort(rightArr)

        # merge
        i = 0 # left array index
        j = 0 # right array index
        k = 0 # merged array index

        while i < len(leftArr) and j < len(rightArr):
            # place which value is bigger on the index k, then increment merged array index k
            if leftArr[i] < rightArr[j]: 
                arr[k] = leftArr[i]
                i += 1
            else:
                arr[k] = rightArr[j]
                j += 1
            k += 1
        
        # assigning the unmerged values to the merged array
        while i < len(leftArr):
            arr[k] = leftArr[i]
            i += 1
            k += 1
        
        while j < len(rightArr):
            arr[k] = rightArr[j]
            j += 1
            k += 1
        
        print(arr)

def quickSort(arr, left, right):
    if left < right: # run code if subarray has atleast 2 elements
        partition_pos = partition(arr, left, right)
        print(arr)
        quickSort(arr, left, partition_pos - 1) # calls quicksort on elements that are less than pivot element
        quickSort(arr, partition_pos + 1, right) # calls quicksort on elements that are greater than pivot element

def partition(arr, left, right): # returns index of every pivot element
    i = left # index left of the pivot
    j = right - 1 # index right of the pivot
    pivot = arr[right] # index of initial pivot

    while i < j:
        # while i is not at the end of the array and element at i is not less than pivot increment i 
        while i < right and arr[i] < pivot: 
            i += 1
        # similar with the above, but minus is used beacuse j is moved to the left 
        while j > left and arr[j] >= pivot: 
            j -= 1
        if i < j: # if they don't cross yet
            arr[i], arr[j] = arr[j], arr[i] # swap

    if arr[i] > pivot: # after i and j cross
        arr[i], arr[right] = arr[right], arr[i] # swap

    return i

arrayValues = [49, 7, 31, 29, 58, 20, 95, 83, 60, 81]
quickSort(arrayValues, 0, len(arrayValues) - 1)
print('Quick Sort: ', arrayValues)