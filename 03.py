from random import randint

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        lft = arr[:mid]
        rgt = arr[mid:]
        merge_sort(lft)
        merge_sort(rgt)
        i = j = k = 0
        while i < len(lft) and j < len(rgt):
            if lft[i] < rgt[j]:
                arr[k] = lft[i]
                i += 1
            else:
                arr[k] = rgt[j]
                j += 1
            k += 1
        while i < len(lft):
            arr[k] = lft[i]
            i += 1
            k += 1
        while j < len(rgt):
            arr[k] = rgt[j]
            j += 1
            k += 1
        return arr

array = [randint(1, 100) for _ in range(10)]
print(array)
print(merge_sort(array))