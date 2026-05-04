from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        freq = defaultdict(int)
        for num in nums:
            freq[num] +=1
        bucket = [[] for i in range(n+1)]
        for num, val in freq.items():
            print(val)
            bucket[val].append(num)
        cnt = k
        ret = []
        for i in range(n,0,-1):
            if cnt == 0:
                return ret
            elif bucket[i]:
                for elt in bucket[i]:
                    ret.append(elt)
                    cnt -= 1
        return ret
            
        

        