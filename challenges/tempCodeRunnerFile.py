def find_duplicate(nums):
    nums = validade_param(nums)
    counter = []

    for n in nums:
        for count in counter:
            if n not in count:
                counter.append(n + 1)


print(find_duplicate([1, 4, 6, 7, 8, 5, 3, 3]))


def validade_param(nums):
    if nums is None:
        return False
    if type(nums) == str:
        return False
    if len(nums) <= 1:
        return False
    if nums <= 1:
        return False
    else:
        return nums
