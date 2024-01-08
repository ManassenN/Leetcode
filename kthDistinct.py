def kthDistinct(arr,k):
    distinct_list = []

    for val in arr:
        if val in distinct_list:
            distinct_list.remove(val)
            continue
        else:
            distinct_list.append(val)

    if len(distinct_list) >= k:
        return distinct_list[k-1]
    else:
        return ""
    

arr = ["d","b","c","b","c","a"]
k = 2
kthDistinct(arr,2)