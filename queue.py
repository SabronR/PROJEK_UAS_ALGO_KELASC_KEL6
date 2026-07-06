from Model import Lagu

class QueueNode:
    def __init__(self, lagu_obj):
        self.data = lagu_obj
        self.next = None
        
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
        
    def is_empty(self):
        return self.front is None
    
    def enqueue(self, lagu_obj):
        if not isinstance(lagu_obj, Lagu):
            print("Error: Data harus berupa objek dari class Lagu!")
            return
        
        node = QueueNode(lagu_obj)
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
        
        return node.data
    
    def peek(self):
        if self.is_empty():
            return None
        return self.front.data
    
    def display(self):
        if self.is_empty():
            print("Antrean permintaan kosong.")
            return
        
        print("--- Antrean Permintaan Pemutaran ---")
        cur = self.front
        i = 1
        while cur:
            Lagu = cur.data
            print(f"{i}. {Lagu.judul} - {Lagu.artis} (ID: {Lagu.id_lagu})")
            cur = cur.next
            i += 1