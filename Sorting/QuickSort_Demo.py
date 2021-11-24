import random
import time
from Algorithm import QuickSort

arr = []

for _ in range(10000):
    arr.append(random.randint(1, 100000))

start_time1 = int(round(time.time() * 1000))
quick_sort_result = QuickSort.QuickSortLomuto().quick_sort(arr)
print("QuickSort: {}ms".format(int(round(time.time() * 1000)) - start_time1))

start_time2 = int(round(time.time() * 1000))
arr.sort()
print("Python sort: {}ms".format(int(round(time.time() * 1000)) - start_time2))

print("Result check:{}".format(arr == quick_sort_result))
