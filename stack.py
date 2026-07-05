from Model import Lagu

class NodeStack:
    def __init__(self, lagu):
        self.lagu = lagu
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
    
    def is_empty(self):
        return self.top is None
    
    def push(self, lagu):
        if not isinstance(lagu, Lagu):
            print("Error: Data harus berupa objek dari class Lagu!")
            return
        
        new_node = NodeStack(lagu)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            print("History kosong, tidak ada lagu sebelumnya")
            return None
        
        popped_node = self.top
        self.top = self.top.next
        self.size -= 1
        return popped_node.lagu
    
    def peek(self):
        if self.is_empty():
            return None
        return self.top.lagu
    
    def display(self):
        if self.is_empty():
            print("History pemutaran kosong.")
            return
        
        print("--- History Pemutaran (LIFO) ---")
        current = self.top
        i = 1
        while current:
            lagu = current.lagu
            print(f"{i}. {current.lagu.judul} - {current.lagu.artis} (ID: {current.lagu.id_lagu})")
            current = current.next
            i += 1