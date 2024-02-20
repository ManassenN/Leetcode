def combinationSum(candidates,target):
    result = []
    def dfs(target,sub_candidates,result):
        if target < 0:
            return
        if target == 0:
            sub_candidates.sort()
            if  sub_candidates in result:
                return
            else:
                result.append(sub_candidates)
                return
        
        for val in candidates:
            sub_candidates.append(val)
            dfs(target - val,sub_candidates[:],result)
            sub_candidates.pop()

    dfs(target,[],result)
    return result

print(combinationSum([2,3,6,7],7))


