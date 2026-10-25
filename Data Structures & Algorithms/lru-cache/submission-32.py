class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:  

    def __init__(self, cap):
        self.cap = cap
        self.cache = {}
        self.head = Node(0,0)   # LRU node.next
        self.tail = Node(0,0)   # LRU node.prev

        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        # Remove 
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def _insert(self, node):
        # old_mru <-> tail
        # old_mru <-> new_mru <-> tail

        mru = self.tail.prev
        mru.next = node
        self.tail.prev = node
        self.tail.prev.next = self.tail
        self.tail.prev.prev = mru


    def get(self, key):
        if key in self.cache:
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].val
        
        return -1
    
    def put(self, key, val):
        if key in self.cache:
            self._remove(self.cache[key])
        
        self.cache[key] = Node(key, val)
        self._insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)