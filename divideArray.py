def divideArray(nums,k):        
        output = []
        nums.sort()

        for i in range(0,len(nums),3):
            temp = []
            if nums[i+1] - nums[i] <= k  and nums[i+2] - nums[i+1] <= k and nums[i+2] - nums[i] <= k :
                temp.append(nums[i])
                temp.append(nums[i+1])
                temp.append(nums[i+2])
            else:
                return []     
            output.append(temp)            
        return output

nums = [15,13,12,13,12,14,12,2,3,13,12,14,14,13,5,12,12,2,13,2,2]
divideArray(nums,2)