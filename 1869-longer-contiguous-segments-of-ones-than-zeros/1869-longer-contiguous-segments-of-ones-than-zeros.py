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
                # print("ch",lz)
                if ln>mn:
                    mn=ln
                ln=0
                lz+=1
        if lz>mz:
            mz=lz
        if ln>mn:
            mn=ln
        print(mn,mz)
        return True if mn>mz else False