test_array = [1,11, 77, 9, 8, 10, 666, 12, 23, 2]
#Bubble Sort O(n^2) run time 
def bubbleSort(array):
    array_length = len(array) 
    for i in range(array_length):
        for j in range(0, array_length-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array
print (bubbleSort(test_array))

#Merge Sort O(nlogn)
def mergeSort(array):
    if len(array) >1: 
        mid = len(array)//2 
        left = array[:mid] 
        right = array[mid:] 
        mergeSort(left) # sort left side
        mergeSort(right) # sort right side
        i = j = k = 0
        # add data to temp arrays 
        while i < len(left) and j < len(array): 
            if left[i] < right[j]: 
                array[k] = left[i] 
                i+=1
            else: 
                array[k] = right[j] 
                j+=1
            k+=1
        while i < len(left): 
            array[k] = left[i] 
            i+=1
            k+=1
          
        while j < len(right): 
            array[k] = right[j] 
            j+=1
            k+=1
        return array 
print (mergeSort(test_array))  



# Partition takes last elemnt as pivot and places everything smaller
# left of the pivot 
def partition(array, low, high):
    i = low-1 #index of smaller element
    pivot = array[high] #assign the pivot
    for j in range(low, high):
        #if current is smaller or equal to pviot
        if array[j] <= pivot:
            i +=1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return (i+1)

def quickSort(array, low, high):
    if low < high:
        p = partition(array, low, high)
        quickSort(array, low, p-1)
        quickSort(array, p+1, high)
n = len(test_array)
quickSort(test_array, 0, n-1)
print ("Sorted array is:") 
for i in range(n): 
    print ("%d" %test_array[i])