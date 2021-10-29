import random
import time
import main


arr = []
for _ in range(100000):
    arr.append(random.randint(1, 10000))

start_time = int(round(time.time() * 1000))
quick_sort_result = main.quick_sort(arr)
end_time = int(round(time.time() * 1000))

start_time2 = int(round(time.time() * 1000))
arr.sort()
end_time2 = int(round(time.time() * 1000))
print("quick_sort: {}ms".format(end_time - start_time))
print("py_sort: {}ms".format(end_time2 - start_time2))
print("result check:{}".format(arr == quick_sort_result))