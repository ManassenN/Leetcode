def maxSubarrayLength(nums,k):
    cache = {}
    length = 0

    for val in nums:
        length += 1
        if val in cache:
            if cache[val] >= k:
                return length - 1
            else:
                cache[val] += 1
        else:
            cache[val] = 1
                            

    return length


maxSubarrayLength([2,2,3],1)