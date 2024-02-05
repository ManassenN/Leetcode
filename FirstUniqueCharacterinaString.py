def firstUniqChar(s):
    char_count = {char: s.count(char) for char in set(s)}

    for i in range(len(s)):
        if char_count[s[i]] == 1:
            return i
        
s = 'loveleetcode'
firstUniqChar(s)