class Node:
    def __init__(self,key,val):
        self.key,self.val = key,val
        self.prev = self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left,self.right = Node(0,0), Node(0,0)
        self.left.nxt = self.right
        self.right.prev = self.left
    
    def remove(self, node: Node) -> None:
        prev,nxt = node.prev,node.nxt
        prev.nxt,nxt.prev = nxt,prev
    
    def insert(self, node: Node) -> None:
        prev,nxt = self.right.prev, self.right
        prev.nxt = node
        nxt.prev = node
        node.prev,node.nxt = prev, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.nxt
            self.remove(lru)
            del self.cache[lru.key]
        
