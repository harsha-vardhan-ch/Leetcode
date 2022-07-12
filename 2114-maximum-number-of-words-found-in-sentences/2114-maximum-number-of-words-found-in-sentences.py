class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        r = [len(x.split(" ")) for x in sentences]
        return max(r)