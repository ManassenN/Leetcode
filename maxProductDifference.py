def maxProductDifference(nums):
    nums.sort()
    pair_one = nums[0] * nums[1]
    pair_two = nums[len(nums) - 1] * nums[len(nums) - 2]
    return pair_two - pair_one
