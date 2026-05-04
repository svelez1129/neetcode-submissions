class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars1 = [0 for i in range(26)]
        p1 = 0
        for c in s:
            pos = ord(c)-97
            chars1[pos]+=1
        for c in t:
            pos = ord(c)-97
            chars1[pos]-=1
        for num in chars1:
            if num != 0:
                return False
        return True
