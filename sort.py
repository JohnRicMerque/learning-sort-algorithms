arrayValues = [49, 7, 31, 29, 58, 20, 95, 83, 60, 81]

def selectionSort(arr):
    for i in range (9): # loop through array indexes
        minpos = i # initially declared minimum position as the i
        for j in range(i, 10): # nested loop starting from i index to the rest
            if arr[j] < arr[minpos]: # if value at index j is less than value at index min position
                minpos = j # reassigns value of minimum position to j
    
    print(minpos)


selectionSort(arrayValues)