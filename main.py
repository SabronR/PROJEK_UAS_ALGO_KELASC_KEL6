from Model import Lagu
from bst import BinarySearchTree
from queue import Queue
from stack import Stack
from max_heap import MaxHeap

if __name__ == "__main__":
    # Inisialisasi struktur data
    katalog_bst = BinarySearchTree()
    antrean_user_queue = Queue()
    prioritas_putar_heap = MaxHeap()
    riwayat_stack = Stack()

    daftar_lagu = [
       Lagu("L001", "Hati-Hati di Jalan", "Tulus", "Manusia", "Pop", "4:02"),
        Lagu("L002", "Sial", "Mahalini", "Fabula", "Pop", "4:15"),
    ]
    for lagu in daftar_lagu:
        katalog_bst.insert(lagu)

    print("=== SIMULASI STREAMING MUSIK ===")
    # User request masuk ke antrian
    print("\n[+] User melakukan request pemutaran lagu...")
    antrean_user_queue.enqueue(daftar_lagu[0], is_premium=False) # Hati-Hati di Jalan
    antrean_user_queue.enqueue(daftar_lagu[1], is_premium=True)  # Sial
    antrean_user_queue.display()

    # 4. Sistem memproses Queue dan memasukkan ke Heap berdasarkan prioritas
    print("\n[+] Sistem memproses antrean ke sistem prioritas (Heap)...")
    while not antrean_user_queue.is_empty():
        lagu_req, is_premium = antrean_user_queue.dequeue()

        lagu_valid = katalog_bst.search(lagu_req.judul)
        if lagu_valid:
            # Hitung prioritas
            skor = 100 if is_premium else 50
            prioritas_putar_heap.insert(lagu_valid, skor)

    prioritas_putar_heap.display()

    # 5. Sistem memutar lagu dari Heap (Tertinggi dulu) dan menyimpan ke Stack (riwayat)
    print("\n[+] Memutar lagu berdasarkan prioritas tertinggi...")
    while prioritas_putar_heap.peek() is not None:
        teratas = prioritas_putar_heap.extract_max()
        lagu_diputar = teratas['lagu']
        print(f"🎵 Sedang memutar: {lagu_diputar.judul} - {lagu_diputar.artis}")
        
        riwayat_stack.push(lagu_diputar)

    # 6. Menampilkan Riwayat & Fitur Undo
    print("\n[+] Cek Riwayat Pemutaran:")
    riwayat_stack.display()

    print("\n[+] User menekan tombol 'Previous' (Undo)...")
    lagu_sebelumnya = riwayat_stack.pop()
    if lagu_sebelumnya:
        print(f"Kembali ke lagu : {lagu_sebelumnya.judul}")