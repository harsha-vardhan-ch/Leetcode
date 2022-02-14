class Solution:
    def mostCommonWord(self, para: str, banned: List[str]) -> str:
        for c in "!?',;.": 
            para = para.replace(c, " ")
        par=para.lower()
        print(par)
        d=Counter(par.split(' ')).most_common()
        print(d)
        for i in d:
            if i[0]!='' and i[0] not in banned :
                return i[0]