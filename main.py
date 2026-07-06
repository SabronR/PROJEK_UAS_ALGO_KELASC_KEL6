
from integrasisitem import MusicStreamingApp

if __name__ == "__main__":
    app = MusicStreamingApp()

    app.tambah_lagu_ke_katalog("L001", "Hati-Hati di Jalan", "Tulus", "Manusia", "Pop", "4:02")
    app.tambah_lagu_ke_katalog("L002", "Sial", "Mahalini", "Single", "Pop", "4:15")
    app.tambah_lagu_ke_katalog("L003", "Monokrom", "Tulus", "Monokrom", "Pop", "3:40")
    app.tambah_lagu_ke_katalog("L004", "Komang", "Raim Laode", "Single", "Pop", "3:42")

    while True:
        print("\n" + "=" * 45)
        print("      SISTEM SIMULASI STREAMING MUSIK")
        print("=" * 45)
        print("1. Tambah Lagu Baru ke Katalog (BST)")
        print("2. Lihat Semua Katalog Lagu (Urut A-Z)")
        print("3. Request Pemutaran Lagu (Masuk Queue)")
        print("4. Proses Antrean ke Sistem Prioritas (Heap)")  
        print("5. Putar Lagu Berdasarkan Prioritas Tertinggi")
        print("6. Cek Status Semua Antrean & Heap")
        print("7. Lihat Riwayat Pemutaran Lagu (History)")
        print("8. Kembalikan ke Lagu Sebelumnya (Undo/Previous)")
        print("9. Keluar Aplikasi")
        print("=" * 45)
        
        pilihan = input("Pilih menu (1-9): ").strip()

        if pilihan == "1":
            print("\n--- TAMBAH LAGU BARU ---")
            id_lagu = input("Masukkan ID Lagu : ").strip()
            judul = input("Masukkan Judul   : ").strip()
            artis = input("Masukkan Artis   : ").strip()
            album = input("Masukkan Album   : ").strip()
            genre = input("Masukkan Genre   : ").strip()
            durasi = input("Masukkan Durasi  : ").strip()
            app.tambah_lagu_ke_katalog(id_lagu, judul, artis, album, genre, durasi)

        elif pilihan == "2":
            app.tampilkan_katalog()

        elif pilihan == "3":
            print("\n--- REQUEST PEMUTARAN LAGU ---")
            judul = input("Masukkan Judul Lagu yang ingin diputar: ").strip()
            app.request_putar_lagu(judul)

        elif pilihan == "4":
            print("\n--- MEMPROSES ANTREAN REQUEST ---")
            app.proses_antrean_ke_heap()  

        elif pilihan == "5":
            print("\n--- PEMUTARAN LAGU TERTINGGI ---")
            app.putar_lagu_teratas()

        elif pilihan == "6":
            print("\n--- STATUS ANTREAN & HEAP ---")
            app.tampilkan_antrean()
            app.tampilkan_prioritas()

        elif pilihan == "7":
            print("\n--- RIWAYAT PEMUTARAN (STACK) ---")
            app.tampilkan_riwayat()

        elif pilihan == "8":
            print("\n--- FITUR UNDO / PREVIOUS ---")
            app.undo_pemutaran()

        elif pilihan == "9":
            print("\nTerima kasih!")
            break
        else:
            print("\nPilihan tidak valid!")