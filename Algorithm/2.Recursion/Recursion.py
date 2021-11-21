def factorial(x: int) -> int:
    if x == 1:
        return x
    else:
        return x * factorial(x - 1)


def list_sum_1(in_nums: list) -> int:
    nums = in_nums[:]
    if len(nums) == 1:
        return nums[0]
    else:
        nums[0] += nums.pop(1)
        return list_sum_1(nums)


def list_sum_2(in_nums: list) -> int:
    nums = in_nums[:]
    if len(nums) == 1:
        return nums[0]
    else:
        return nums.pop() + list_sum_2(nums)
