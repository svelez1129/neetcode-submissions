from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        ls = c.most_common(k)
        ret = []
        for tup in ls:
            ret.append(tup[0])
        return ret

        