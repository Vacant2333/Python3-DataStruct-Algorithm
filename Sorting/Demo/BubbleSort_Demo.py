from Sorting.Algorithm.BubbleSort import BubbleSort1, BubbleSort2

arr = [1, 99, 43, 26, 84, 29, 10, 24, 10, 23, 55, -2, -90, 0, 95, 28, 82, 6, 4, 12, 9]

bs1_result = BubbleSort1().run(arr)
bs2_result = BubbleSort2().run(arr)
sorted_result = sorted(arr)

print("BubbleSort1 result:{}".format(bs1_result))
print("BubbleSort2 result:{}".format(bs2_result))
print("Check result:{}, {}".format(bs1_result == sorted_result, bs2_result == sorted_result))
