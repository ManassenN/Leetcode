def permute(nums):
    res = []

    #Base case
    if (len(nums) == 1):
        return [nums.copy()]

    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permute(nums)

        for perm in perms:
            perm.append(n)
        res.extend(perms)
        nums.append(n)

    return res

print(permute([1,2,3,4]))