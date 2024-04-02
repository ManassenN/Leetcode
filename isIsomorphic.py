def isIsomorphic(s,t):
    s_to_t = {}  # Cache to map characters from s to t
    t_to_s = {}  # Cache to map characters from t to s
    
    for i in range(len(s)):
        s_char = s[i]
        t_char = t[i]
        
        # Check if s_char is already mapped to a different character in t
        if s_char in s_to_t:
            if s_to_t[s_char] != t_char:
                return False
        else:
            s_to_t[s_char] = t_char
        
        # Check if t_char is already mapped to a different character in s
        if t_char in t_to_s:
            if t_to_s[t_char] != s_char:
                return False
        else:
            t_to_s[t_char] = s_char
    
    return True


isIsomorphic('badc','baba')