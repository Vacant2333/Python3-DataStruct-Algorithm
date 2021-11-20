class QuickSortLomuto:
    # QuickSort(Lomuto version)
    def quick_sort(self, big_list: list[int]) -> list:
        if len(big_list) <= 1:
            return big_list
        else:
            partition_result = self.partition(big_list)
            # print(partition_result)
            return self.quick_sort(partition_result['left']) + [partition_result['pivot']] + self.quick_sort(partition_result['right'])

    # Divide list and return pivot
    def partition(self, big_list: list[int]) -> dict:
        plist = big_list.copy()
        left = []
        right = []
        pivot = plist.pop(0)
        for value in plist:
            if value >= pivot:
                right.append(value)
            else:
                left.append(value)
        return {'left': left, 'pivot': pivot, 'right': right}
