import time
from main import SelectionSort

arr = [10, 234, 43, 31, 44, 321, 342, 123, 124, 355, 789, 77, 65, 54, 65]

ss = SelectionSort()

print(ss.selection_sort(arr, 1))

start_time = int(round(time.time() * 1000))