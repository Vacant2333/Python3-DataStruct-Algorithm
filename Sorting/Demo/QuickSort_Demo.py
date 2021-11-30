from Sorting.Algorithm.QuickSort import QuickSortLomuto

arr = [1, 99, 43, 26, 84, 29, 10, 24, 10, 23, 55]

quick_sort_result = QuickSortLomuto().run(arr)
print("QuickSort result:{}".format(quick_sort_result))

sorted_result = sorted(arr)
print("Sorted result:{}".format(sorted_result))
