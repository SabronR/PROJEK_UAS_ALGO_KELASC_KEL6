from Model import Lagu

class QueueNode:
    def __init__(self, lagu_obj, is_premium=False):
        self.data = lagu_obj
        self.is_premium = is_premium
        self.next = None
        
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
        
    def is_empty(self):
        return self.front is None
    
    def enqueue(self, lagu_obj, is_premium=False):
        if not isinstance(lagu_obj, Lagu):
            print("Error: Data harus berupa objek dari class Lagu!")
            return
        
        node = QueueNode(lagu_obj, is_premium)
        if self.rear is None:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self.size += 1
        
    def dequeue(self):
        if self.is_empty():
            return None
        node = self.front
        self.front = node.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        
        return node.data, node.is_premium
    
    def peek(self):
        if self.is_empty():
            return None
        return self.front.data, self.front.is_premium
    
    def display(self):
        if self.is_empty():
            print("Antrean permintaan kosong.")
            return
        
        print("--- Antrean Permintaan Pemutaran ---")
        cur = self.front
        i = 1
        while cur:
            Lagu = cur.data
            label = "Premium" if cur.is_premium else "Reguler"
            
            print(f"{i}. {Lagu.judul} - {Lagu.artis} (ID: {Lagu.id_lagu}) [{label}]")
            cur = cur.next
            i += 1