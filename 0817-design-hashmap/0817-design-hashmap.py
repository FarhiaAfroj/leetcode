class ListNode:
    def __init__(self, key=-1, value=-1, next=None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.buckets = [ListNode() for _ in range(self.size)]
    
    def _hash(self, key):
        return key % self.size
    
    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        current = self.buckets[index]
        
        while current.next:
            if current.next.key == key:
                current.next.value = value
                return
            current = current.next
        
        current.next = ListNode(key, value)
    
    def get(self, key: int) -> int:
        index = self._hash(key)
        current = self.buckets[index].next
        
        while current:
            if current.key == key:
                return current.value
            current = current.next
        
        return -1
    
    def remove(self, key: int) -> None:
        index = self._hash(key)
        current = self.buckets[index]
        
        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next