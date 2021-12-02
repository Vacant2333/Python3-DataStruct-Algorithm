class BubbleSort1:
    def run(self, ar: list[int]) -> list[int]:
        arr = ar[:]
        # End flag, it will return if no action in 1 loop
        flag = True
        while flag:
            flag = False
            for index, value in enumerate(arr):
                if index != len(arr) - 1 and arr[index + 1] < arr[index]:
                    # If the next item smaller than now, exchange them
                    arr[index], arr[index + 1] = arr[index + 1], arr[index]
                    # May more actions, continue
                    flag = True
        return arr


# Better than 1
class BubbleSort2:
    def run(self, ar: list[int]) -> list[int]:
        arr = ar[:]
        # End flag, it will return if no action in 1 loop
        flag = True
        for now_round in range(1, len(arr)):
            if flag == False:
                break
            # If there is no action, exit the loop in advance
            flag = False
            # The last value of each round is the largest
            for index in range(0, len(arr) - now_round):
                if arr[index] > arr[index + 1]:
                    arr[index], arr[index + 1] = arr[index + 1], arr[index]
                    flag = True
        return arr
