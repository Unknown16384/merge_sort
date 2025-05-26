import timeit
from random import randint

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
        return arr
def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pvt = arr[len(arr) // 2]
    lft = [x for x in arr if x < pvt]
    mid = [x for x in arr if x == pvt]
    rgt = [x for x in arr if x > pvt]
    return quick_sort(lft) + mid + quick_sort(rgt)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i
        while j > 0 and arr[j - 1] > key:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = key
    return arr

def compare(n):
    arr = [randint(1, 100) for _ in range(n)]
    if merge_sort(arr) == bubble_sort(arr):
        a = timeit.timeit(lambda: merge_sort(arr), number=1000)
        b = timeit.timeit(lambda: bubble_sort(arr), number=1000)
        print(f'merge_sort: {a:.6}; bubble_sort: {b:.6}')
compare(10)
compare(100)
compare(1000)