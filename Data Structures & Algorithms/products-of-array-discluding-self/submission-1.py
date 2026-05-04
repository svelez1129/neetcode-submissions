class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        #check how many zeroes there are, if more than two zeroes everything is just zero
        zeroRet = [0 for i in range(n)]
        zeroCnt = 0
        for num in nums:
            if num == 0:
                zeroCnt += 1
            if zeroCnt > 1:
                return zeroRet 
       #do prefix mult
        prefix = [nums[i] for i in range(n)]
        for i in range(1,n):
            prefix[i] *= prefix[i-1]
        #do suffix mult
        suffix = [nums[i] for i in range(n)]
        for j in range(n-2,0,-1):
            suffix[j] *= suffix[j+1]
        ret = []
        for i in range(n):
            if i == 0:
                ret.append(suffix[i+1])
            elif i == n-1:
                ret.append(prefix[i-1])
            else:
                ret.append(prefix[i-1]*suffix[i+1])
        return ret