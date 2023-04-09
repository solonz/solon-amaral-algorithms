def find_duplicate(nums):
    if not isinstance(nums, list) or len(nums) < 2:
        return False

    counter = {}
    for num in nums:
        if not isinstance(num, int) or num < 1:
            return False
        if num in counter:
            return num
        counter[num] = 1
    return False
