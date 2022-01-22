class MyCircularQueue:
    i=0
    def __init__(self, k: int):
        self.a=[]
        self.max_size=k
        return
    
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.a.append(value)
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        del self.a[0]
        return True

    def Front(self) -> int:
        print(self.a)
        if self.isEmpty():
            print("in front empty")
            return -1
        print("in else of front")
        return self.a[0]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.a[-1]
    
    def isEmpty(self) -> bool:
        if len(self.a)==0:
            #print("in empty")
            return True
        return False

    def isFull(self) -> bool:
        if len(self.a)==self.max_size:
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()