from Sorting.Algorithm.InsertSort import InsertSort

arr = [1, 99, 43, 26, 84, 29, 10, 24, 10, 23, 55, -2, -90, 0, 95, 28, 82, 6, 4, 12, 9]

is_result = InsertSort().run(arr)
sorted_result = sorted(arr)

print("InsertSort result:{}".format(is_result))
print("Check result:{}".format(sorted_result == is_result))
