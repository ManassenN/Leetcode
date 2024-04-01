def countSubarrays(nums,k):
    output = 0
    l , r = 0 , 0 
    max_val = max(nums)

    while l < len(nums):
        current_array = nums[l:r]
        if r == len(nums):
            r = l
            l += 1
        r+=1    
        if current_array.count(max_val) >= k:
            output += 1
            continue
        else:
            continue

    return output


countSubarrays([1,4,2,1] , k = 2)

            

        