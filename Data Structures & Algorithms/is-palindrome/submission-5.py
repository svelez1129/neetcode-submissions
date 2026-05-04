class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        l = 0
        r = n-1
        while l < r:
            print(s[l])
            print(s[r])
            while not s[l].isalnum():  
                l+=1
                if l >= r:
                    return True
            while not s[r].isalnum():
                r-=1
                if l >= r:
                    return True
            if l >= r:
                break
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True