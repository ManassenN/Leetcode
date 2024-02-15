def largestPerimeter(nums):
        nums.sort()
        j ,sum1 = len(nums) - 1, 0

        while 0 < j:
            sum1 = sum(nums[0:j])
            if sum1 > nums[j]:
                return sum1 + nums[j]
            else:
                j = j - 1       

        return -1         

nums = [5,5,50]
largestPerimeter(nums)
