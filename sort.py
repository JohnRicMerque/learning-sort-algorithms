def selectionSort(arr):
    for i in range (9): # loop through array indexes
        minpos = i # initially declared minimum position as the i
        for j in range(i, 10): # nested loop starting from i index to the rest
            if arr[j] < arr[minpos]: # if value at index j is less than value at index min position
                minpos = j # reassigns value of minimum position to j

        # this code below switches the array value from the one we declared min position, with the one we found to be minimum value. the loop will search for the minimum value to the right, not including the values in the previous iterations, which were the minimum values found prior.
        temp = arr[i] 
        arr[i] = arr[minpos] # replace the new minimim value in index of initially considered minimum value
        arr[minpos] = temp # put the replaced value in the initial index of minimum value

arrayValues = [49, 7, 31, 29, 58, 20, 95, 83, 60, 81]
selectionSort(arrayValues)
print(arrayValues)