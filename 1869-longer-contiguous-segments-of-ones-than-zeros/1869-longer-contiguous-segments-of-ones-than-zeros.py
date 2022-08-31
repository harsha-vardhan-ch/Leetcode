class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        lz=0
        ln=0
        mz=0
        mn=0
        for i in s:
            if i=="1":
                if lz>mz:
                    mz=lz
                lz=0
                ln+=1
            elif i=="0":
                if ln>mn:
                    mn=ln
                ln=0
                lz+=1
    
        mz=max(lz,mz)
        mn=max(ln,mn)
        return True if mn>mz else False