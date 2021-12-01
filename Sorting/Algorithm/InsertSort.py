class InsertSort:
    def get_smaller_value_index(self, ar: list[int], check_value: int) -> int:
        # Reverse the list and get a smaller index
        for index in range(1, len(ar) + 1):
            if ar[index * -1] < check_value:
                return len(ar) + (-1 * index) + 1
        # The check_value is the smallest one, insert it in index 0
        return 0

    def run(self, ar: list[int]) -> list[int]:
        arr = ar[:]
        for index in range(1, len(arr)):
            # Pop 1 item and insert back
            value = arr.pop(index)
            # Insert value into the list where a <= value < b
            arr.insert(self.get_smaller_value_index(arr[:index], value), value)
            print(arr[:index], self.get_smaller_value_index(arr[:index], value), value, arr)
        return arr
