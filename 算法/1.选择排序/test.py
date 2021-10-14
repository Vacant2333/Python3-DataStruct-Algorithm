import random
import time
from main import SelectionSort

ss = SelectionSort()
arr = []

start_time = int(round(time.time() * 1000))

for _ in range(100000):
    arr.append(random.randint(1, 100000))

ss_result = ss.selection_sort(arr)
ss_time = int(round(time.time() * 1000))
print("选择排序耗时:{}毫秒".format(ss_time - start_time))
py_result = sorted(arr, reverse=True)
py_time = int(round(time.time() * 1000))
print("py sorted排序耗时:{}毫秒".format(py_time - ss_time))
print(py_result == ss_result)
