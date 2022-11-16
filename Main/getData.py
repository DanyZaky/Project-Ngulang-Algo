import os

class GetData():
    def __init__(self):
        self.dataAdminDirectory = os.path.join(os.path.dirname(__file__), "CSV File/Data Admin.csv")
        self.dataLapPengeluaranDirectory = os.path.join(os.path.dirname(__file__), "CSV File/Data Laporan Keuangan Pengeluaran.csv")
        self.dataLapPenjualanDirectory = os.path.join(os.path.dirname(__file__), "CSV File/Data Laporan Keuangan Penjualan.csv")
        self.dataStokGudangDirectory = os.path.join(os.path.dirname(__file__), "CSV File/Data Stok Gudang.csv")
        self.dataStokPenyortirannDirectory = os.path.join(os.path.dirname(__file__), "CSV File/Data Stok Penyortiran.csv")
        self.dataStokProdukJadiDirectory = os.path.join(os.path.dirname(__file__), "CSV File/Data Stok Produk Jadi.csv")