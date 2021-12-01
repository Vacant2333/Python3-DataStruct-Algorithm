from Sorting.Algorithm.BubbleSort import BubbleSort1, BubbleSort2

arr = [5, 1, 2, 4, 2, 10, 23, 5, 12, 8, 21, 9]
bs1_result = BubbleSort1().run(arr)
bs2_result = BubbleSort2().run(arr)
print("BubbleSort1 result:{}".format(bs1_result))
print("BubbleSort2 result:{}".format(bs2_result))

sorted_result = sorted(arr)
print("Check result:{}, {}".format(bs1_result == sorted_result, bs2_result == sorted_result))
