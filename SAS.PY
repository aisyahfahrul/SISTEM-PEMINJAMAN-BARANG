class Barang:
    def __init__(self, kode_barang, nama_barang, stok):
        self.kode_barang = kode_barang
        self.nama_barang = nama_barang
        self.stok = stok

class Peminjaman:
    def __init__(self):
        self.daftar_barang = {}
        self.data_peminjaman = []

    # CRUD Barang
    def tambah_barang(self):
        kode_barang = input("Masukkan kode barang: ")
        if kode_barang in self.daftar_barang:
            print("Kode barang sudah ada!")
            return
        nama_barang = input("Masukkan nama barang: ")
        stok = int(input("Masukkan jumlah stok: "))
        self.daftar_barang[kode_barang] = Barang(kode_barang, nama_barang, stok)
        print("Barang berhasil ditambahkan.")

    def lihat_barang(self):
        if not self.daftar_barang:
            print("Tidak ada barang yang tersedia.")
        else:
            print("Daftar Barang:")
            for barang in self.daftar_barang.values():
                print(f"Kode: {barang.kode_barang}, Nama: {barang.nama_barang}, Stok: {barang.stok}")

    def ubah_barang(self):
        kode_barang = input("Masukkan kode barang yang ingin diubah: ")
        if kode_barang not in self.daftar_barang:
            print("Barang tidak ditemukan!")
            return
        nama_barang = input("Masukkan nama barang baru (kosongkan jika tidak ingin mengubah): ")
        stok = input("Masukkan jumlah stok baru (kosongkan jika tidak ingin mengubah): ")
        if nama_barang:
            self.daftar_barang[kode_barang].nama_barang = nama_barang
        if stok:
            self.daftar_barang[kode_barang].stok = int(stok)
        print("Barang berhasil diubah.")

    def hapus_barang(self):
        kode_barang = input("Masukkan kode barang yang ingin dihapus: ")
        if kode_barang in self.daftar_barang:
            del self.daftar_barang[kode_barang]
            print("Barang berhasil dihapus.")
        else:
            print("Barang tidak ditemukan!")

    # CRUD Peminjaman
    def tambah_peminjaman(self):
        kode_barang = input("Masukkan kode barang yang dipinjam: ")
        if kode_barang not in self.daftar_barang:
            print("Barang tidak ditemukan!")
            return
        jumlah = int(input("Masukkan jumlah barang yang dipinjam: "))
        if self.daftar_barang[kode_barang].stok < jumlah:
            print("Stok barang tidak mencukupi!")
            return
        nama_peminjam = input("Masukkan nama peminjam: ")
        self.daftar_barang[kode_barang].stok -= jumlah
        self.data_peminjaman.append({
            "kode_barang": kode_barang,
            "nama_peminjam": nama_peminjam,
            "jumlah": jumlah
        })
        print("Peminjaman berhasil ditambahkan.")

    def lihat_peminjaman(self):
        if not self.data_peminjaman:
            print("Belum ada data peminjaman.")
        else:
            print("Data Peminjaman:")
            for i, data in enumerate(self.data_peminjaman, 1):
                print(f"{i}. Peminjam: {data['nama_peminjam']}, Barang: {data['kode_barang']}, Jumlah: {data['jumlah']}")

    def hapus_peminjaman(self):
        self.lihat_peminjaman()
        if not self.data_peminjaman:
            return
        index = int(input("Masukkan nomor data peminjaman yang ingin dihapus: ")) - 1
        if 0 <= index < len(self.data_peminjaman):
            peminjaman = self.data_peminjaman.pop(index)
            self.daftar_barang[peminjaman['kode_barang']].stok += peminjaman['jumlah']
            print("Data peminjaman berhasil dihapus.")
        else:
            print("Data peminjaman tidak ditemukan!")

# Program Utama
def main():
    sistem = Peminjaman()
    while True:
        print("\n=== Sistem Peminjaman Barang ===")
        print("1. Tambah Barang")
        print("2. Lihat Barang")
        print("3. Ubah Barang")
        print("4. Hapus Barang")
        print("5. Tambah Peminjaman")
        print("6. Lihat Peminjaman")
        print("7. Hapus Peminjaman")
        print("0. Keluar")
        pilihan = input("Pilih menu: ")
        
        if pilihan == "1":
            sistem.tambah_barang()
        elif pilihan == "2":
            sistem.lihat_barang()
        elif pilihan == "3":
            sistem.ubah_barang()
        elif pilihan == "4":
            sistem.hapus_barang()
        elif pilihan == "5":
            sistem.tambah_peminjaman()
        elif pilihan == "6":
            sistem.lihat_peminjaman()
        elif pilihan == "7":
            sistem.hapus_peminjaman()
        elif pilihan == "0":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
