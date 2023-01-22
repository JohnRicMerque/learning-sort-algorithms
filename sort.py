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


arrayValues = [49, 7, 31, 29, 58, 20, 95, 83, 60, 81]
insertionSort(arrayValues)
print('Insertion Sort: ', arrayValues)