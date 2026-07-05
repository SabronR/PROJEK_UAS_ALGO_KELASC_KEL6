from Model import Lagu

class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i - 1) // 2
    
    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2
    
    def insert(self, lagu, skor):
        elemen = {'lagu': lagu, 'skor': skor}
        self.heap.append(elemen)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, i):
        while i > 0 and self.heap[self.parent(i)]['skor'] < self.heap[i]['skor']:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)
    
    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root
    
    def _heapify_down(self, i):
        max_idx = i
        left = self.left_child(i)
        right = self.right_child(i)
        n = len(self.heap)

        if left < n and self.heap[left]['skor'] > self.heap[max_idx]['skor']:
            max_idx = left
        if right < n and self.heap[right]['skor'] > self.heap[max_idx]['skor']:
            max_idx = right

        if i != max_idx:
            self.heap[i], self.heap[max_idx] = self.heap[max_idx], self.heap[i]
            self._heapify_down(max_idx)
        
    def peek(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]
    
    def display(self):
        if len(self.heap) == 0:
            print("Antrian Prioritas kosong.")
            return
        
        print("--- Antrian Prioritas (Max Heap) ---")
        for i, item in enumerate(self.heap):
            print(f"{i + 1}. {item['lagu'].judul} [Skor: {item['skor']}]")
