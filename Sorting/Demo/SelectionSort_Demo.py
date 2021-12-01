from Sorting.Algorithm.SelectionSort import SelectionSort1, SelectionSort2

arr = [121, 15, 42, 17, 19, 122, 55, 30, 12, 55, 21]

ss1_result = SelectionSort1().run(arr)
ss2_result = SelectionSort2().run(arr)
sorted_result = sorted(arr)

print("SS1 result:{}".format(ss1_result))
print("SS2 result:{}".format(ss2_result))
print("Check result:{}, {}".format(ss1_result == sorted_result, ss2_result == sorted_result))

