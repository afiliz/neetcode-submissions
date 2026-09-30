class Node:
    def __init__(self, key: int, val: int):
        self.next = None
        self.prev = None
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def moveToHead(self, key: int) -> None:
        before_key = self.cache[key].prev
        after_key = self.cache[key].next
        if before_key:
            before_key.next = after_key
        if after_key:
            after_key.prev = before_key

        self.cache[key].next = self.head.next
        self.cache[key].prev = self.head
        self.head.next.prev = self.cache[key]
        self.head.next = self.cache[key]

    def removeLRU(self) -> None:
        lru = self.tail.prev
        lru_key = lru.key
        
        lru.prev.next = self.tail
        self.tail.prev = lru.prev

        del self.cache[lru_key]

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.moveToHead(key)
            return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.moveToHead(key)
        else:
            if len(self.cache) == self.capacity:
                self.removeLRU()
            self.cache[key] = Node(key, value)
            self.moveToHead(key)
