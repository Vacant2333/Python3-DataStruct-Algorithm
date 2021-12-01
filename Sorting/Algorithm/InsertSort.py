class InsertSort:
    def get_smaller_value_index(self, ar: list[int], check_value: int) -> int:
        # Reverse the list and get a smaller index
        for index in range(1, len(ar) + 1):
            if ar[index * -1] < check_value:
                return len(ar) + (-1 * index) + 1
        return len(ar) - 1

    def run(self, ar: list[int]) -> list[int]:
        arr = ar[:]
        for index in range(1, len(arr)):
            value = arr.pop(index)
            arr.insert(self.get_smaller_value_index(arr[:index], value), value)
        return arr
