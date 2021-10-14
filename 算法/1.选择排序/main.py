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

    def selection_sort(self, arr: list, sort: int = 1) -> list:
        # 选择排序 sort :0升序 1降序
        new_arr, key, smallest_key = [[], None, 0]
        for key in range(len(arr)):
            smallest_key = self.find_smallest_value(arr)
            new_arr.append(arr[smallest_key])
            arr[smallest_key] = None
        return new_arr if sort == 0 else new_arr[::-1]
