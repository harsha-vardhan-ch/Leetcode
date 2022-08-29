class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}
        for index, val in enumerate(order):
            order_map[val] = index
        # print(order_map)
        for i in range(len(words)-1):
            # t=min(len(words[i]),len(words[i+1]))
            for j in range(len(words[i])):
                # For cases like "apple", "app"
                if j>=len(words[i+1]):
                    return False
                if words[i][j]!=words[i+1][j]:
                    # if greater => not sorted, so return False
                    if order_map[words[i][j]]>order_map[words[i+1][j]]:
                        return False
                    # if less than => in sorted order [ < ] , no further checking needed
                    break
        return True
            
        """
        T.C - O(n) => n=numbet of characters in entire words list
        S.C - O(1) => For dict
        """
            