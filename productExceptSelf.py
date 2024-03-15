from numpy import *
# an o(n^2) solution.
def productExceptSelf(nums):
    output = []

    def helper(list):
        return prod(list)
    
    for i in range(len(nums)):
        copy_list = nums.copy()
        copy_list.pop(i)
        output.append(helper(copy_list))


    return output

print(productExceptSelf([-1,1,0,-3,3])) 