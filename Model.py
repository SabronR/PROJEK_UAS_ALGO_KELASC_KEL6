class Lagu:
    def __init__(self, id_lagu, judul, artis, album, genre, durasi):
        self.id_lagu = id_lagu
        self.judul = judul
        self.artis = artis
        self.album = album
        self.genre = genre
        self.durasi = durasi

    def tampil(self):
        print(f"ID     : {self.id_lagu}")
        print(f"Judul  : {self.judul}")
        print(f"Artis  : {self.artis}")
        print(f"Album  : {self.album}")
        print(f"Genre  : {self.genre}")
        print(f"Durasi : {self.durasi}")
        print("-" * 35)
