class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left = None   # LRU
        self.right = None  # MRU

    def remove(self, node):
        # Only node
        if node.left is None and node.right is None:
            self.left = None
            self.right = None

        # Remove LRU
        elif node == self.left:
            self.left = node.right
            self.left.left = None

        # Remove MRU
        elif node == self.right:
            self.right = node.left
            self.right.right = None

        # Remove middle
        else:
            node.left.right = node.right
            node.right.left = node.left

        node.left = None
        node.right = None

    def append(self, node):
        # Empty
        if self.right is None:
            self.left = node
            self.right = node
            return

        node.left = self.right
        self.right.right = node
        self.right = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Promote to MRU
        self.remove(node)
        self.append(node)

        return node.val

    def put(self, key: int, value: int) -> None:

        # Existing key
        if key in self.cache:
            node = self.cache[key]
            node.val = value

            self.remove(node)
            self.append(node)
            return

        # New key
        node = Node(key, value)
        self.cache[key] = node
        self.append(node)

        # Remove LRU if over capacity
        if len(self.cache) > self.capacity:
            lru = self.left
            self.remove(lru)
            del self.cache[lru.key]