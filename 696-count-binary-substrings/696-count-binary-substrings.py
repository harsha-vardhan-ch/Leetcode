class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = [1]
        for i in range(1, len(s)):
            # If not equal increment, else add 1 
            if s[i-1] != s[i]:
                groups.append(1)
            else:
                groups[-1] += 1
                
        # print(groups) => if  s = "110001111000000" => groups = [ 2, 3, 4, 6]
        ans=0
        for i in range(1,len(groups)):
            ans+=min(groups[i-1],groups[i])
        return ans
    
        