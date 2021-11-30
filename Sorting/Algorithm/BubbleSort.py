class BubbleSort:
    def run(self, ar: list[int]) -> list[int]:
        arr = ar[:]
        # End flag,it will return if no action in 1 loop
        flag = True
        while flag:
            flag = False
            for index, value in enumerate(arr):
                if index != len(arr) - 1 and arr[index + 1] < arr[index]:
                    # If the next item smaller than now,exchange them
                    arr[index], arr[index + 1] = arr[index + 1], arr[index]
                    # May more actions,continue
                    flag = True
        return arr
