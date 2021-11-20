def factorial(x):
    if x == 1:
        return x
    else:
        return x * factorial(x - 1)


def list_sum(nums: list):
    if len(nums) == 1:
        return nums[0]
    else:
        nums[0] += nums.pop(1)
        return list_sum(nums)


def list_sum_2(nums: list):
    if len(nums) == 1:
        return nums[0]
    else:
        return nums.pop() + list_sum_2(nums)
