class SelectionSort:
    # 选择排序

    def find_smallest_value(self, arr: list) -> int:
        # 返回最小值的索引 数组为空则返回-1
        smallest_key, key = [None, 0]
        for key in range(len(arr)):
            if arr[key] is not None:
                if smallest_key is not None:
                    if arr[key] < arr[smallest_key]:
                        smallest_key = key
                else:
                    smallest_key = key
        return smallest_key

    def selection_sort(self, ar: list, sort: int = 1) -> list:
        # 选择排序 sort :0升序 1降序
        arr = ar[:]
        new_arr, key, smallest_key = [[], None, 0]
        for key in range(len(arr)):
            smallest_key = self.find_smallest_value(arr)
            new_arr.append(arr[smallest_key])
            arr[smallest_key] = None
        return new_arr if sort == 0 else new_arr[::-1]

# 优化后
class SelectionSort2:
    # 选择排序

    def find_smallest_value(self, arr: list) -> int:
        # 返回最小值的索引 数组为空则返回-1
        min_value: int = 999999
        min_value_index: int = 0
        for index, value in enumerate(arr):
            if value < min_value:
                min_value_index = index
                min_value = value
        return arr.pop(min_value_index)

    def selection_sort(self, ar: list, sort: int = 1) -> list:
        # 选择排序 sort :0升序 1降序
        arr = ar[:]
        new_arr, key, smallest_key = [[], None, 0]
        for key in range(len(arr)):
            new_arr.append(self.find_smallest_value(arr))
        return new_arr if sort == 0 else new_arr[::-1]
