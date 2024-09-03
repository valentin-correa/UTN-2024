def BubbleSort(array):
    length = len(array) - 1
    ac = 0
    for i in range(length):
        for j in range(length):
            if array[j] > array [j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                ac += 1
    return array, ac

def InsertSort(array):
    length = len(array)
    ac = 0
    for i in range(1, length):
        insert_value = array[i]
        insert_index = i
        while insert_index > 0 and array[insert_index - 1] > insert_value:
            array[insert_index] = array[insert_index - 1]
            insert_index -= 1
            ac += 1
        array[insert_index] = insert_value
    return array, ac

def quicksort(array, ini, fin):
    if ini < fin:
        pivot = division (array, ini, fin)
        quicksort(array, ini, pivot - 1)
        quicksort(array, pivot + 1, fin)

def division(array, ini, fin):
    i = ini
    j = fin - 1
    pivot = array[fin]

    while i < j:
        while i < fin and array[i] < pivot:
            i+=1
        
        while j > ini and array[j] >= pivot:
            j-=1

        if i < j:
            array[i], array[j] = array[j], array[i]
    
    if array[i] > pivot:
        array[i], array[fin] = array[fin], array[i]

    return i

vector = [1,4,8,5,6,9,7,2,3]
quicksort(vector, 0, len(vector)-1)
print(vector)