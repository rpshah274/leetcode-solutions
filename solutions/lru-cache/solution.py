# Problem: LRU Cache
# URL: https://leetcode.com/problems/lru-cache/
# Language: python3

class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev=self.next=None

class LRUCache:
    def __init__(self, capacity: int):
        self.LRUCache={}
        self.cap=capacity
        self.oldest= Node(0,0)
        self.latest= Node(0,0)
        self.oldest.next=self.latest
        self.latest.prev=self.oldest

    def remove(self,node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self,node):
        prev,nxt=self.oldest,self.oldest.next
        node.prev = prev
        node.next = nxt
        prev.next = node
        nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.LRUCache:
            self.remove(self.LRUCache[key])
            self.insert(self.LRUCache[key])
            return self.LRUCache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.LRUCache:
            self.remove(self.LRUCache[key])
        self.LRUCache[key]=Node(key,value)
        self.insert(self.LRUCache[key])

        if len(self.LRUCache)>self.cap:
            lru=self.latest.prev
            self.remove(lru)
            del self.LRUCache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)