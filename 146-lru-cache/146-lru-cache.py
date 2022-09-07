from collections import OrderedDict
class LRUCache:
    # cache = 
    remain=0
    def __init__(self, capacity: int):
        self.remain = capacity
        self.cache=collections.OrderedDict()
        print()

    def get(self, key: int) -> int:
        # print(self)
        if key not in self.cache:
            return - 1
        # accessed key, so bringing it to end
        self.cache.move_to_end(key)
        # print(self.cache,self.cache[key])
        # since it is in end, returning it directly
        return self.cache[key]


    def put(self, key: int, value: int) -> None:
        
        if key in self.cache:
            self.cache.move_to_end(key)
            # print(key,self.cache,"bef")
        self.cache[key] = value
        # print(self.cache)
        if len(self.cache) > self.remain:
            self.cache.popitem(last = False) # evicting the first 



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)