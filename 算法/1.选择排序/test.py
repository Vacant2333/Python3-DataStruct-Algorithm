import random
import time
from main import SelectionSort, SelectionSort2
ss = SelectionSort()
ss2 = SelectionSort2()
arr = []

start_time = int(round(time.time() * 1000))

for _ in range(10):
    arr.append(random.randint(1, 100000))

ss_result = ss.selection_sort(arr)
ss_time = int(round(time.time() * 1000))
print("选择排序耗时:{}毫秒".format(ss_time - start_time))

py_result = sorted(arr, reverse=True)
py_time = int(round(time.time() * 1000))
print("py sorted排序耗时:{}毫秒".format(py_time - ss_time))

ss2_result = ss2.selection_sort(arr)
ss2_time = int(round(time.time() * 1000))
print("选择排序2耗时:{}毫秒".format(ss2_time - py_time))

print(py_result == ss_result)
print(py_result == ss2_result)