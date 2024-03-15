def numSubarraysWithSum(nums,goal):
    i , j = 0 , 0
    sum = 0
    count = 0 
    while i < len(nums):
        if sum == goal and (i!=j): count += 1
        if j == len(nums) or sum > goal:
            i = i + 1
            j = i
            sum = 0 
            continue
        

        if i == j:
            sum += nums[j]
            j = j + 1
            continue
        else:
            sum += nums[j]
            j = j + 1
            continue    


    return count

arr = [1,0,1,0,1]
numSubarraysWithSum(arr,2)    