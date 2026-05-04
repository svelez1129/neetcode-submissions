class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ret = []
        seen = {}
        for i in range(len(strs)):
            curr = "".join(sorted(strs[i]))
            if curr in seen:
                seen[curr].append(strs[i])
            else:
                seen[curr] = [strs[i]]
        for val in seen.values():
            ret.append(val)
        return ret