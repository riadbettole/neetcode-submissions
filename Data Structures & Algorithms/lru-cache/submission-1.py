class ListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}  
        
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node: ListNode) -> None:
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node: ListNode) -> None:
        prev, nxt = self.tail.prev, self.tail
        prev.next = node
        nxt.prev = node
        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            new_node = ListNode(key, value)
            self.dic[key] = new_node
            self.insert(new_node)
            
            if len(self.dic) > self.capacity:
                lru_node = self.head.next
                self.remove(lru_node)
                del self.dic[lru_node.key] 


    
