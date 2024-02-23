
def findLeastNumOfUniqueInts(arr,k):
    element_counts = {element:arr.count(element) for element in arr}
    dict_values = sorted(element_counts.values())
    
    # Matching Sorted values to decrease from k times
    for val in dict_values:
        for key in element_counts:
            if element_counts[key] == val:
                if element_counts[key] > k:
                    element_counts[key] = element_counts[key] - k
                    k = 0
                    break
                else:
                    k = k - element_counts[key]
                    element_counts.pop(key)
                    break 
        if k == 0:
            break            
    
    return len(set(element_counts))


findLeastNumOfUniqueInts(arr,k)


    