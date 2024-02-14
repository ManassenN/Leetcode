def rearrangeArray(self, nums: List[int]) -> List[int]:
    nums_pos = [val for val in nums if val > 0]
    nums_neg = [val for val in nums if val < 0]

    rearranged_array = []
    for _ in range(len(nums_pos)):
        rearranged_array.append(nums_pos[_])
        rearranged_array.append(nums_neg[_])
        
    return rearranged_array