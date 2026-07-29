import os
import time

class Node:
   
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.next = None

class AdvancedHashMap:
    
    def __init__(self, capacity: int = 8):
        self.cap = capacity
        self.size = 0
        self.table = [None] * self.cap
        self.ratio = 0.75

    def _hash(self, key) -> int:
        return (hash(key) ^ (hash(key) >> 16)) & (self.cap - 1)

    def put(self, key, value) -> None:
        if self.size / self.cap >= self.ratio:
            self._resize()

        idx = self._hash(key)
        curr = self.table[idx]
        
        while curr:
            if curr.key == key:
                curr.val = value
                self.visualize(f"UPDATED: '{key}' -> '{value}' at bucket [{idx}]")
                return
            curr = curr.next

        new_node = Node(key, value)
        new_node.next = self.table[idx]
        self.table[idx] = new_node
        self.size += 1
        self.visualize(f"INSERTED: '{key}' -> '{value}' into bucket [{idx}]")

    def get(self, key):
        idx = self._hash(key)
        curr = self.table[idx]
        
        while curr:
            if curr.key == key:
                self.visualize(f"FOUND: '{key}' in bucket [{idx}]")
                return curr.val
            curr = curr.next
            
        self.visualize(f"ERROR: Key '{key}' not found!")
        raise KeyError(str(key))

    def _resize(self) -> None:
        self.visualize("i love mmom HashMap is resizing...")
        time.sleep(1)
        
        old_table = self.table
        self.cap <<= 1
        self.table = [None] * self.cap
        self.size = 0  
        
        for node in old_table:
            while node:
              
                k, v = node.key, node.val 
                node = node.next  
                self.put(k, v)

    def visualize(self, event_msg: str = "") -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=" * 60)
        print(" i love  mmom HashMap ")
        print("=" * 60)
        print(f" Status     : {event_msg}")
        print(f" Load Factor: {self.size}/{self.cap} ({self.size/self.cap:.2f} / Threshold: {self.ratio})")
        print("-" * 60)
        
        for idx in range(self.cap):
            bucket_line = f" Bucket [{idx:02d}]: "
            nodes = []
            curr = self.table[idx]
            while curr:
                nodes.append(f"[{curr.key}: {curr.val}]")
                curr = curr.next
            if nodes:
                bucket_line += " ➔ " + " ➔ ".join(nodes) + " ➔ None"
            else:
                bucket_line += " ∅ (Empty)"
            print(bucket_line)
            
        print("=" * 60)
        time.sleep(0.6)


if __name__ == "__main__":
    hm = AdvancedHashMap(capacity=4)
    sample_data = [
        ("mmmom", "Dev  in my dream clock "),
        ("me", "Designing my dream clock"),
        ("Calvvin", "QA"),
        ("fela", "CEO"),
        ("fela", "Manager"),
        ("i   love mmomy", "me"),
        ("e", "Lead mmom"),
        ("f", "is me")
    ]
    
    for k, v in sample_data:
        hm.put(k, v)
        
    try:
        hm.get("Charlie")
        hm.get("Zack")
    except KeyError:
        pass
