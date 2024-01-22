
def findErrorNums(nums):
        nums_copy = nums[:]
        nums_copy.sort()
        duplicates = []
        
        for i in range(len(nums_copy)):
                if i+1 < len(nums_copy) and nums_copy[i] == nums_copy[i+1]:
                        duplicates.append(nums_copy[i])
                        nums_copy[i+1] = nums_copy[i+1]
                        break

        for val in range(1, len(nums_copy)+1):
                if val in nums_copy:
                        continue
                else:
                        duplicates.append(val)                
        return duplicates

nums = [2,2]
print(findErrorNums(nums))