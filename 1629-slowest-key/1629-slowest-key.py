class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        res=releaseTimes[0]
        ch=keysPressed[0]
        
        for i in range(1,len(releaseTimes)):
            dur=releaseTimes[i]-releaseTimes[i-1]
            if res<dur:
                res=dur
                ch=keysPressed[i]
            elif res==dur:
                if ord(ch)<ord(keysPressed[i]):
                    ch=keysPressed[i]
                print(res,ch,keysPressed[i])
        return ch
            