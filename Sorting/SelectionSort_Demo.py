import random
import time
from Algorithm import SelectionSort

arr = []

for _ in range(10000):
    arr.append(random.randint(1, 100000))

# Start speed test
start_time = int(round(time.time() * 1000))

# SelectionSort version 1
ss1_result = SelectionSort.SelectionSort1().selection_sort(arr)
ss1_time = int(round(time.time() * 1000))
print("SelectionSort_1:{}ms".format(ss1_time - start_time))

# SelectionSort version 2
ss2_result = SelectionSort.SelectionSort2().selection_sort(arr)
ss2_time = int(round(time.time() * 1000))
print("SelectionSort_2:{}ms".format(ss2_time - ss1_time))

py_result = sorted(arr, reverse=True)
py_time = int(round(time.time() * 1000))
print("Python sorted:{}ms".format(py_time - ss2_time))

# Check result
print("Result check 1:{}".format(py_result == ss1_result))
print("Result check 2:{}".format(py_result == ss2_result))
