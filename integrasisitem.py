from Model import Lagu
from bst import BinarySearchTree
from queue import Queue
from max_heap import MaxHeap
from stack import Stack

class MusicStreamingApp:
    def __init__(self):
        self.katalog_bst = BinarySearchTree()
        self.antrean_queue = Queue()       
        self.prioritas_heap = MaxHeap()     
        self.riwayat_stack = Stack()        
        self.skor_antrean = 1000            

    def tambah_lagu_ke_katalog(self, id_lagu, judul, artis, album, genre, durasi):
        lagu = Lagu(id_lagu, judul, artis, album, genre, durasi)
        self.katalog_bst.insert(lagu)
        print(f"[Sukses] Lagu '{judul}' berhasil ditambahkan ke katalog.")

    def request_putar_lagu(self, judul_lagu):
        lagu = self.katalog_bst.search(judul_lagu)
        if lagu is None:
            print(f"[Gagal] Lagu '{judul_lagu}' tidak ditemukan di katalog.")
            return

        self.antrean_queue.enqueue(lagu)
        print(f"[Selesai] '{lagu.judul}' berhasil masuk antrean request.")

    def proses_antrean_ke_heap(self):
        def proses_antrean_ke_heap(self):
            if self.antrean_queue.is_empty():
                print("[Info] Tidak ada antrean request di Queue saat ini.")
                return
    
        self.skor_antrean = 1000 
        
        print("Memindahkan data dari antrean ke prioritas...")
        while not self.antrean_queue.is_empty():
            lagu_req = self.antrean_queue.dequeue()

            self.prioritas_heap.insert(lagu_req, self.skor_antrean)
            self.skor_antrean -= 1 
            
        print("[Selesai] Semua antrean telah dipindahkan ke prioritas (Max Heap).")

    def putar_lagu_teratas(self):
        if self.prioritas_heap.peek() is None:
            print("[Info] Tidak ada lagu di antrean prioritas untuk diputar.")
            return

        teratas = self.prioritas_heap.extract_max()
        lagu_diputar = teratas['lagu']
        
        print(f"🎵 NOW PLAYING: {lagu_diputar.judul} - {lagu_diputar.artis}")
        
        self.riwayat_stack.push(lagu_diputar)

    def undo_pemutaran(self):
        lagu_sebelumnya = self.riwayat_stack.pop()
        if lagu_sebelumnya:
            print(f"⏮️ UNDO: Kembali memutar '{lagu_sebelumnya.judul}' - {lagu_sebelumnya.artis}")

    def tampilkan_katalog(self):
        print("\n=== KATALOG LAGU (BST URUT A-Z) ===")
        self.katalog_bst.inorder()

    def tampilkan_antrean(self):
        self.antrean_queue.display()

    def tampilkan_prioritas(self):
        self.prioritas_heap.display()

    def tampilkan_riwayat(self):
        self.riwayat_stack.display()