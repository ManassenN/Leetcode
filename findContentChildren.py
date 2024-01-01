
def findContentChildren(self, g: List[int], s: List[int]) -> int:
    # Sort with built-in function with complexity of O(nlogn).
    g.sort(reverse = True)
    s.sort(reverse = True)
    res, i , j = 0 ,0,0
    # Traverse the array with O(n) running time.
    while i<len(g) and j<len(s):
        if g[i]<=s[j]:
            res+=1
            i+=1
            j+=1
        else:
            i+=1
    return res