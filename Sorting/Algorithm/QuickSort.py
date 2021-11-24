class QuickSortLomuto:
    # QuickSort(Lomuto version)
    def quick_sort(self, in_list: list[int]) -> list:
        if len(in_list) <= 1:
            return in_list
        else:
            partition_result = self.partition(in_list)
            # print(partition_result)
            return self.quick_sort(partition_result['left']) + [partition_result['pivot']] + self.quick_sort(partition_result['right'])

    # Divide list and return pivot
    def partition(self, in_list: list[int]) -> dict:
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
