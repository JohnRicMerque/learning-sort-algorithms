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

arrayValues = [49, 7, 31, 29, 58, 20, 95, 83, 60, 81]
selectionSort(arrayValues)
print(arrayValues)