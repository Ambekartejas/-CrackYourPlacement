class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n=len(needle)
        if needle in haystack:
            for i in range(len(haystack)-n+1):
                if needle==haystack[i:i+n]:
                    return i
        else:
            return -1
            
            
        