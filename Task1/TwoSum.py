nums = [2, 7, 11, 15]
target = 9


def two_sum(nums, target):
    for digit in nums:
        for dig in nums:
            if digit + dig == target:
                return [nums.index(digit), nums.index(dig)]


print(two_sum(nums, target))
