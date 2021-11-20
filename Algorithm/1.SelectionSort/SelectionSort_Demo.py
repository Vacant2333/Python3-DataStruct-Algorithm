import random
import time
import SelectionSort

ss = SelectionSort.SelectionSort1()
ss2 = SelectionSort.SelectionSort2()
arr = []

start_time = int(round(time.time() * 1000))

for _ in range(1000):
    arr.append(random.randint(1, 100000))

ss_result = ss.selection_sort(arr)
ss_time = int(round(time.time() * 1000))
print("SelectionSort_1:{}ms".format(ss_time - start_time))

py_result = sorted(arr, reverse=True)
py_time = int(round(time.time() * 1000))
print("Python sorted:{}ms".format(py_time - ss_time))

ss2_result = ss2.selection_sort(arr)
ss2_time = int(round(time.time() * 1000))
print("SelectionSort_2:{}ms".format(ss2_time - py_time))

print(py_result == ss_result)
print(py_result == ss2_result)
