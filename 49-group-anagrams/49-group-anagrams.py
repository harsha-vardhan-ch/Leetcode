class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)
        for s in strs:
            #print(type(s),s)
            key = ''.join(sorted(s))
            #print(type(key),key)
            groups[key].append(s)
        print(groups)
        return groups.values()