class Solution:
    def capitalizeTitle(self, tit: str) -> str:
        a=[i.title() if len(i)>2 else i.lower() for i in tit.split(" ")]
        return ' '.join(a)