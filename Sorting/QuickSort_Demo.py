import random
import time
from Sorting.Algorithm import QuickSort

arr = []
for _ in range(100000):
    arr.append(random.randint(1, 10000))

qs = QuickSort.QuickSortLomuto()

start_time = int(round(time.time() * 1000))
quick_sort_result = qs.quick_sort(arr)
end_time = int(round(time.time() * 1000))

start_time2 = int(round(time.time() * 1000))
arr.sort()
end_time2 = int(round(time.time() * 1000))
print("QuickSort: {}ms".format(end_time - start_time))
print("Python sort: {}ms".format(end_time2 - start_time2))
print("result check:{}".format(arr == quick_sort_result))
