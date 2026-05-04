class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []
        seen = {}
        for i in range(len(strs)):
            counter = [0 for i in range(26)]
            for c in strs[i]:
                pos = ord(c)-97
                counter[pos]+=1
            curr = tuple(counter)
            if curr in seen:
                seen[curr].append(strs[i])
            else:
                seen[curr] = [strs[i]]
        for val in seen.values():
            ret.append(val)
        return ret