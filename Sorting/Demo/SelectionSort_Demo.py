from Sorting.Algorithm.SelectionSort import SelectionSort1, SelectionSort2

arr = [1, 99, 43, 26, 84, 29, 10, 24, 10, 23, 55, -2, -90, 0, 95, 28, 82, 6, 4, 12, 9]

ss1_result = SelectionSort1().run(arr)
ss2_result = SelectionSort2().run(arr)
sorted_result = sorted(arr)

print("SS1 result:{}".format(ss1_result))
print("SS2 result:{}".format(ss2_result))
print("Check result:{}, {}".format(ss1_result == sorted_result, ss2_result == sorted_result))

