class QuickSortLomuto:
    # QuickSort(Lomuto version)
    def run(self, in_list: list[int]) -> list[int]:
        if len(in_list) <= 1:
            return in_list
        else:
            partition_result = self.__partition(in_list)
            return self.run(partition_result['left']) + [partition_result['pivot']] + self.run(partition_result['right'])

    # Divide list and return pivot
    def __partition(self, in_list: list[int]) -> dict:
        plist = in_list[:]
        left = []
        right = []
        pivot = plist.pop(0)
        for value in plist:
            if value >= pivot:
                right.append(value)
            else:
                left.append(value)
        return {'left': left, 'pivot': pivot, 'right': right}
