def missingNumber(nums):
        input_array_sum = sum(nums) 
        desired_sum = 0
        for i in range(len(nums)+1):
            desired_sum += i
        print("here")    
        return desired_sum - input_array_sum 

missingNumber([9,6,4,2,3,5,7,0,1])