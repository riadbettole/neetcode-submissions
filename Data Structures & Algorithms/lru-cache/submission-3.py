class DoubleListNode:
    def __init__(self, key=0, val=0):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  
        
        self.head, self.tail = DoubleListNode(0, 0), DoubleListNode(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head

    def remove(self, node: DoubleListNode) -> None:
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node: DoubleListNode) -> None:
        prev, nxt = self.tail.prev, self.tail
        prev.next = nxt.prev = node
        node.prev, node.next= prev, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            
        self.cache[key] = DoubleListNode(key, value)
        self.insert(self.cache[key])
            
        if len(self.cache) > self.cap:
            lru_node = self.head.next
            self.remove(lru_node)
            del self.cache[lru_node.key] 

