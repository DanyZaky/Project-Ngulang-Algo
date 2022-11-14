import os
import pandas as pd

from manipulation import Manipulation as CRUD

class GetData():
    def __init__(self):
        self.dataAdminDirectory = os.path.join(os.path.dirname(__file__), "CSV File/Data Admin.csv")
        self.dataLapPengeluaranDirectory = os.path.join(os.path.dirname(__file__), "CSV File/Data Laporan Keuangan Pengeluaran.csv")
        self.dataLapPenjualanDirectory = os.path.join(os.path.dirname(__file__), "CSV File/Data Laporan Keuangan Penjualan.csv")
        self.dataStokGudangDirectory = os.path.join(os.path.dirname(__file__), "CSV File/Data Stok Gudang.csv")
        self.dataStokPenyortirannDirectory = os.path.join(os.path.dirname(__file__), "CSV File/Data Stok Penyortiran.csv")
        self.dataStokProdukJadiDirectory = os.path.join(os.path.dirname(__file__), "CSV File/Data Stok Produk Jadi.csv")

class SystemUI():
    def __init__(self):
        self.mainMenu = "=================================================\n===== SISTEM ADMINISTASI CV. SEMANGAT JAYA ======\n=================================================\n= 1. Kelola Data Admin                          =\n= 2. Kelola Data Laporan Keuangan Pengeluaran   =\n= 3. Kelola Data Laporan Keuangan Penjualan     =\n= 4. Kelola Data Stok Gudang                    =\n= 5. Kelola Data Stok Penyortiran               =\n= 6. Kelola Data Stok Produk Jadi               =\n=================================================\n> "

    def clearScreen(self):
        os.system('cls')

getData = GetData()
systemUI = SystemUI()
crud = CRUD()

class RunSystem():
    def __init__(self):
        self.setMainMenu = None
        self.systemIsRunning = True
    
    def run(self):
        systemUI.clearScreen()
        self.setMainMenu = input(str(systemUI.mainMenu))
        systemUI.clearScreen()
        if (self.setMainMenu == "1"):
            crud.readData(getData.dataAdminDirectory)
        elif (self.setMainMenu == "2"):
            crud.readData(getData.dataLapPengeluaranDirectory)
        elif (self.setMainMenu == "3"):
            crud.readData(getData.dataLapPenjualanDirectory)
        elif (self.setMainMenu == "4"):
            crud.readData(getData.dataStokGudangDirectory)
        elif (self.setMainMenu == "5"):
            crud.readData(getData.dataStokPenyortirannDirectory)
        elif (self.setMainMenu == "6"):
            crud.readData(getData.dataStokProdukJadiDirectory)

rs = RunSystem()
rs.run()