def bagOfTokensScore(tokens,power):
    max_score = 0
    score = 0
    # Sort in O(nlogn)
    tokens.sort()
    r,l = len(tokens) - 1 , 0

    
    while l <= r :
    # Try greedy approach , and if possible, play Face-up.    
        if power >= tokens[l]:
            power -= tokens[l]
            score += 1
            l+=1
            max_score = max(score,max_score)    
            continue
        elif score >=1:            
    # Else, Try to play Face-Down from the right end of the list
            power += tokens[r]
            score -= 1
            r -= 1
            continue
        else:
            return 0    
    return max_score
bagOfTokensScore([71,55,82],54)