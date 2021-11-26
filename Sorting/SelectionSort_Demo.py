from Algorithm.SelectionSort import SelectionSort1, SelectionSort2

arr = [121, 15, 42, 17, 19, 122, 55, 30, 12, 55, 21]

ss1_result = SelectionSort1().run(arr)
print("SS1 result:{}".format(ss1_result))

ss2_result = SelectionSort2().run(arr)
print("SS2 result:{}".format(ss2_result))

sorted_result = sorted(arr)
print("Sorted result:{}".format(sorted_result))
