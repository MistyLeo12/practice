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
    return array 

