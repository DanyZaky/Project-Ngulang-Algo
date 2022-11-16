import os

class SystemUI():
    def __init__(self):
        self.mainMenu = "=================================================\n===== SISTEM ADMINISTASI CV. SEMANGAT JAYA ======\n=================================================\n[1] Kelola Data Admin\n[2] Kelola Data Laporan Keuangan Pengeluaran \n[3] Kelola Data Laporan Keuangan Penjualan\n[4] Kelola Data Stok Gudang \n[5] Kelola Data Stok Penyortiran\n[6] Kelola Data Stok Produk Jadi\n[7] Keluar\n> "
        self.selectCRUD = "[1] Lihat Data\n[2] Tambah Data\n[3] Hapus Data\n[4] Kembali\n> "
        self.backPanel = "[1] Kembali\n> "
        self.delete = "Masukkan index baris yang ingin dihapus!\n> "
        self.errorInputPanel = "Masukkan input dengan benar!"

    def clearScreen(self):
        os.system('cls')