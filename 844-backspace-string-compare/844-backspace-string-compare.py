class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_box = []
        t_box = []
        for i in s:
            if i!='#':
                s_box.append(i)
            elif len(s_box)>0:
                del s_box[-1]
        for i in t:
            if i!='#':
                t_box.append(i)
            elif len(t_box)>0:
                del t_box[-1]
        if len(s_box)!=len(t_box):
            return False
        for i in range(len(s_box)):
            if s_box[i]!=t_box[i]:
                return False
        return True
        # print(s_box,t_box)
        