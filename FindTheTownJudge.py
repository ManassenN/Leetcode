def findJudge(n,trust):
    # key: [number of people that i trust, the list of the people]
    hash = {i:[0,[]] for i in range(1,n+1)} 


    for tr in trust:
        hash[tr[1]][1].append(tr[0])
        hash[tr[0]][0] +=1

    for key in hash:
        if hash[key][0] == 0 and len(hash[key][1]) == n-1:
            return key

    return -1        
    
trust = [[1,3],[2,3]]
n = 3
findJudge(n,trust)