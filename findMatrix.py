def findMatrix(nums):
    # Sort the array for creating orderd elements with O(nlogn) runnig time
    nums.sort()
    # Creating the desired matrix
    mat = []
    mat.append([nums[0]])

    for i in range(1,len(nums)):
        not_appended = True
        if nums[i]==nums[i-1]:
            """ Check if the value of nums[i] is in any of the current mat rows , if not
             the we have to create a new row in the matrix  """ 
            for val in mat:
                if nums[i] not in val: # if the value is not in the row val , we can append to it and raise flag accordingly
                    val.append(nums[i])
                    not_appended = False
                    break
                

            #Create a new row
            if not_appended:
                mat.append([nums[i]])    

        else:
            for val in mat:
                if nums[i] not in val:
                    val.append(nums[i])
                    break 

    return mat

nums = [1,3,4,1,2,3,1]
findMatrix(nums)