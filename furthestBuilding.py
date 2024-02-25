def furthestBuilding(heights,bricks,ladders):
<<<<<<< HEAD
    for i in range(len(heights) -1):
        diff = heights[i+1] - heights[i]
        if diff <= 0:
            
=======
    
    i = 0 
    j = i + 1
    output = 0
    while(i < j):
        
        if heights[i] - heights[j] >= 0:
            if j == len(heights)-1:
                output += 1
                break
            i = i + 1
            j = j + 1
            output += 1
            continue
        else:

            if heights[j] - heights[i] <= bricks:
                    bricks -= heights[j] - heights[i]
                    if j == len(heights)-1:
                        output += 1
                        break
                    i = i + 1
                    j = j + 1
                    output += 1
                    continue
            else:
                if ladders > 0:
                    ladders -= 1
                    if j == len(heights)-1:
                        output += 1
                        break
                    i = i + 1
                    j = j + 1
                    output += 1
                    continue
                # If we reached here that means no more bricks and no more ladders, there for we cannot reach the next buliding.
                else:
                     return output
    return output

furthestBuilding([1,5,1,2,3,4,10000],4,1)        
>>>>>>> 0b925892a929b793d3f270f8fd5d1645639de665
