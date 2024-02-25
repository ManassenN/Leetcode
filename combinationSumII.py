def combinationSum2(candidates, target):
    candidates.sort()
    res = []
    def backtrack(cur,i,target):
        if target == 0:
            res.append(cur.copy())
        if target <= 0:
            return

        prev = -1
        for i in range(len(candidates)):
            if candidates[i] == prev:
                continue
            cur.append(candidates[i])
            backtrack(cur,i+1,target - candidates[i])
            cur.pop()
            prev = candidates[i]

        backtrack([],0,target)
        return res    