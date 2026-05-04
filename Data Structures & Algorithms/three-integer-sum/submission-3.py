class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = set()
        nums = sorted(nums)
        for i,num in enumerate(nums):
            target = -num
            l = i+1
            r = len(nums)-1
            while l < r:
                if l >= r:
                    break
                if nums[l]+nums[r] == target:
                    ls = tuple(sorted([nums[l],nums[r],-target]))
                    ret.add(ls)
                    l+=1
                    r-=1
                elif nums[l]+nums[r] < target:
                    l+=1
                else:
                    r-=1
        out = []
        for tup in ret:
            out.append(list(tup))
        return out
    
    