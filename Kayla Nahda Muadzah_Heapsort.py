def heapsort(arr):
    def build_heap(arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            perbaiki_heap(arr, i, n)
    
    def perbaiki_heap(arr, i, heap_size):
        kiri = 2 * i + 1
        kanan = 2 * i + 2
        terbesar = i
        if kiri < heap_size and arr[kiri] > arr[terbesar]:
            terbesar = kiri
        if kanan < heap_size and arr[kanan] > arr[terbesar]:
            terbesar = kanan
        if terbesar != i:
            arr[i], arr[terbesar] = arr[terbesar], arr[i]
            perbaiki_heap(arr, terbesar, heap_size)
    
    n = len(arr)
    build_heap(arr)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        perbaiki_heap(arr, 0, i)
    
    return arr

# contoh penggunaan program
arr = [64, 25, 12, 22, 11]
arr_terurut = heapsort(arr)
print(arr_terurut)
