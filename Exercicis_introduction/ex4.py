
def mergeSort(array):
    if len(array) > 1:

        mid = len(array)//2
        L = array[:mid]
        H = array[mid:]

        mergeSort(L)
        mergeSort(H)

        i = j = k = 0

        while i < len(L) and j < len(H):
            if L[i] <= H[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = H[j]
                j += 1
            k += 1

        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(H):
            array[k] = H[j]
            j += 1
            k += 1

