from Model import Lagu
from bst import BinarySearchTree

if __name__ == "__main__":

    katalog = BinarySearchTree()

    daftar_lagu = [
        Lagu("L001", "Hati-Hati di Jalan", "Tulus", "Manusia", "Pop", "4:02"),
        Lagu("L002", "Sial", "Mahalini", "Single", "Pop", "4:15"),
        Lagu("L003", "Monokrom", "Tulus", "Monokrom", "Pop", "3:40"),
        Lagu("L004", "Komang", "Raim Laode", "Single", "Pop", "3:42"),
        Lagu("L005", "Tak Segampang Itu", "Anggi Marito", "Single", "Pop", "4:10"),
        Lagu("L006", "Blue", "Yung Kai", "Single", "Pop", "3:30")
    ]

    # Menambahkan Lagu ke BST
    for lagu in daftar_lagu:
        katalog.insert(lagu)

    print("=" * 45)
    print("      KATALOG LAGU STREAMING MUSIK")
    print("=" * 45)

    katalog.inorder()

    print("\n")
    print("=" * 45)
    print("PENCARIAN LAGU")
    print("=" * 45)

    cari = "Komang"

    hasil = katalog.search(cari)

    if hasil:
        print(f"Lagu '{cari}' ditemukan!\n")
        hasil.tampil()
    else:
        print("Lagu tidak ditemukan.")
