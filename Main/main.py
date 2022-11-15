import os
import pandas as pd

from manipulation import Manipulation as MP

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
        self.mainMenu = "=================================================\n===== SISTEM ADMINISTASI CV. SEMANGAT JAYA ======\n=================================================\n[1] Kelola Data Admin\n[2] Kelola Data Laporan Keuangan Pengeluaran \n[3] Kelola Data Laporan Keuangan Penjualan\n[4] Kelola Data Stok Gudang \n[5] Kelola Data Stok Penyortiran\n[6] Kelola Data Stok Produk Jadi\n[7] Keluar\n> "
        self.selectCRUD = "[1] Lihat Data\n[2] Tambah Data\n[3] Hapus Data\n[4] Kembali\n> "
        self.backPanel = "[1] Kembali\n> "
        self.errorInputPanel = "Masukkan input dengan benar!"

    def clearScreen(self):
        os.system('cls')

getData = GetData()
systemUI = SystemUI()
mp = MP()

class RunSystem():
    def __init__(self):
        self.inputMainMenu = None
        self.inputSubMenu = None
        self.inputMP = None
        
        self.menuIsRunning = True
        self.subMenuIsRunning = True
        self.mpIsRunning = True

    
    def run(self):
        while (self.menuIsRunning == True):

            self.subMenuIsRunning = True
            self.inputMainMenu = str(input(systemUI.mainMenu))

            if(self.inputMainMenu == "1"):
                while (self.subMenuIsRunning == True):

                    self.inputSubMenu = str(input(systemUI.selectCRUD))

                    if (self.inputSubMenu == "1"):
                        mp.readData(getData.dataAdminDirectory)
                    elif (self.inputSubMenu == "2"):
                        print("tambah")
                    elif (self.inputSubMenu == "3"):
                        print("hapus")
                    elif (self.inputSubMenu == "4"):
                        self.subMenuIsRunning = False
                    else:
                        print(systemUI.errorInputPanel)

            elif(self.inputMainMenu == "2"):
                while (self.subMenuIsRunning == True):

                    self.mpIsRunning = True
                    self.inputSubMenu = str(input(systemUI.selectCRUD))

                    if (self.inputSubMenu == "1"):
                        while (self.mpIsRunning == True):
                            mp.readData(getData.dataLapPengeluaranDirectory)
                            self.inputMP = str(input(systemUI.backPanel))
                            if (self.inputMP == "1"):
                                self.mpIsRunning = False
                            else:
                                print(systemUI.errorInputPanel)

                    elif (self.inputSubMenu == "2"):
                        print("tambah")
                    elif (self.inputSubMenu == "3"):
                        print("hapus")
                    elif (self.inputSubMenu == "4"):
                        self.subMenuIsRunning = False
                    else:
                        print(systemUI.errorInputPanel)

            elif(self.inputMainMenu == "3"):
                print("3")
            elif(self.inputMainMenu == "4"):
                print("4")
            elif(self.inputMainMenu == "5"):
                print("5")
            elif(self.inputMainMenu == "6"):
                print("6")
            elif(self.inputMainMenu == "7"):
                print("Terimakasih dan sehat selalu")
                self.menuIsRunning = False
            else:
                print(systemUI.errorInputPanel)
            


rs = RunSystem()
rs.run()