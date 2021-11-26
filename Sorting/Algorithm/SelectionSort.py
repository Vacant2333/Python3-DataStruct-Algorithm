class SelectionSort1:
    # Return the least key,if list is null then -1
    def get_smallest_value(self, arr: list[int]) -> int:
        smallest_key, key = [None, 0]
        for key in range(len(arr)):
            if arr[key] is not None:
                if smallest_key is not None:
                    if arr[key] < arr[smallest_key]:
                        smallest_key = key
                else:
                    smallest_key = key
        return smallest_key

    def run(self, ar: list[int]) -> list[int]:
        arr = ar[:]
        new_arr, key, smallest_key = [[], None, 0]
        for key in range(len(arr)):
            smallest_key = self.get_smallest_value(arr)
            new_arr.append(arr[smallest_key])
            arr[smallest_key] = None
        return new_arr


# Better than 1
class SelectionSort2:
    # Return the least key,if list is null then -1
    def get_smallest_value(self, arr: list[int]) -> int:
        min_value = float('inf')
        min_value_index = 0
        for index, value in enumerate(arr):
            if value < min_value:
                min_value_index = index
                min_value = value
        return arr.pop(min_value_index)

    def run(self, ar: list[int]) -> list[int]:
        arr = ar[:]
        new_arr, key, smallest_key = [[], None, 0]
        for key in range(len(arr)):
            new_arr.append(self.get_smallest_value(arr))
        return new_arr
