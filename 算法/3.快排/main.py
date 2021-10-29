# 快排Lomuto 按元素分治
def quick_sort(olist: list[int]) -> list:
    if len(olist) <= 1:
        return olist
    else:
        partition_result = partition(olist)
        # 打印过程
        #print(partition_result)
        return quick_sort(partition_result['left']) + [partition_result['pivot']] + quick_sort(partition_result['right'])


# 分割 pivot坐标
def partition(olist: list[int]) -> dict:
    plist = olist.copy()
    left = []
    right = []
    pivot = plist.pop(0)
    for value in plist:
        if value >= pivot:
            right.append(value)
        else:
            left.append(value)
    return {'left': left, 'pivot': pivot, 'right': right}
