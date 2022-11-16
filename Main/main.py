from manipulation import Manipulation
from systemUI import SystemUI
from getData import GetData

getData = GetData()
systemUI = SystemUI()
mp = Manipulation()

class RunSystem():
    def __init__(self):
        self.inputMainMenu = None
        self.inputSubMenu = None
        self.inputMP = None

        self.inputRowDelete = None
        self.tempData = {}
        self.tempInputData = []
        self.tempVarData = []
        
        self.menuIsRunning = True
        self.subMenuIsRunning = True
        self.mpIsRunning = True
    
    def run(self):
        while (self.menuIsRunning == True):

            self.subMenuIsRunning = True
            self.tempData = {}
            self.tempInputData = []
            self.tempVarData = []
            self.inputMainMenu = str(input(systemUI.mainMenu))

            if(self.inputMainMenu == "1"):
                while (self.subMenuIsRunning == True):
                    self.mpIsRunning = True
                    self.inputSubMenu = str(input(systemUI.selectCRUD))

                    if (self.inputSubMenu == "1"):
                        while (self.mpIsRunning == True):
                            mp.readData(getData.dataAdminDirectory)
                            self.inputMP = str(input(systemUI.backPanel))
                            if (self.inputMP == "1"):
                                self.mpIsRunning = False
                            else:
                                print(systemUI.errorInputPanel)

                    elif (self.inputSubMenu == "2"):
                        while (self.mpIsRunning == True):                            
                            self.tempVarData = ['ID', 'Nama', 'Password', 'Nomor Telepon']
                            self.tempInputData = ['','','','']
                            
                            for i in range(0, len(self.tempVarData)):
                                self.tempInputData[i] = str(input("Masukkan " + self.tempVarData[i] + ": "))

                            self.tempData = {
                                'ID' : [self.tempInputData[0]],
                                'Nama' : [self.tempInputData[1]],
                                'Password' : [self.tempInputData[2]],
                                'Nomor Telepon' : [self.tempInputData[3]]
                            }

                            mp.addData(getData.dataAdminDirectory, self.tempData)
                            mp.readData(getData.dataAdminDirectory)
                            print("Data berhasil ditambahkan!")

                            self.inputMP = str(input(systemUI.backPanel))
                            if (self.inputMP == "1"):
                                self.mpIsRunning = False
                            else:
                                print(systemUI.errorInputPanel)
                    
                    elif (self.inputSubMenu == "3"):
                        while (self.mpIsRunning == True):
                            
                            mp.readData(getData.dataAdminDirectory)
                            self.inputRowDelete = int(input(systemUI.delete))
                            
                            mp.deleteData(getData.dataAdminDirectory, int(self.inputRowDelete))
                            mp.readData(getData.dataAdminDirectory)
                            print("Data berhasil dihapus!")

                            self.inputMP = str(input(systemUI.backPanel))
                            if (self.inputMP == "1"):
                                self.mpIsRunning = False
                            else:
                                print(systemUI.errorInputPanel)

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
                        while (self.mpIsRunning == True):                            
                            self.tempVarData = ['Nomor Transaksi', 'Tanggal Pengeluaran', 'Harga Beli', 'Jumlah']
                            self.tempInputData = ['','','','']
                            
                            for i in range(0, len(self.tempVarData)):
                                self.tempInputData[i] = str(input("Masukkan " + self.tempVarData[i] + ": "))

                            self.tempData = {
                                'Nomor Transaksi' : [self.tempInputData[0]],
                                'Tanggal Pengeluaran' : [self.tempInputData[1]],
                                'Harga Beli' : [self.tempInputData[2]],
                                'Jumlah' : [self.tempInputData[3]],
                                'Total Harga' : [str(int(self.tempInputData[2])*int(self.tempInputData[3]))]
                            }

                            mp.addData(getData.dataLapPengeluaranDirectory, self.tempData)
                            mp.readData(getData.dataLapPengeluaranDirectory)
                            print("Data berhasil ditambahkan!")

                            self.inputMP = str(input(systemUI.backPanel))
                            if (self.inputMP == "1"):
                                self.mpIsRunning = False
                            else:
                                print(systemUI.errorInputPanel)
                    
                    elif (self.inputSubMenu == "3"):
                        while (self.mpIsRunning == True):
                            
                            mp.readData(getData.dataLapPengeluaranDirectory)
                            self.inputRowDelete = int(input(systemUI.delete))
                            
                            mp.deleteData(getData.dataLapPengeluaranDirectory, int(self.inputRowDelete))
                            mp.readData(getData.dataLapPengeluaranDirectory)
                            print("Data berhasil dihapus!")

                            self.inputMP = str(input(systemUI.backPanel))
                            if (self.inputMP == "1"):
                                self.mpIsRunning = False
                            else:
                                print(systemUI.errorInputPanel)

                    elif (self.inputSubMenu == "4"):
                        self.subMenuIsRunning = False

                    else:
                        print(systemUI.errorInputPanel)

            elif(self.inputMainMenu == "3"):
                while (self.subMenuIsRunning == True):
                    self.mpIsRunning = True
                    self.inputSubMenu = str(input(systemUI.selectCRUD))

                    if (self.inputSubMenu == "1"):
                        while (self.mpIsRunning == True):
                            mp.readData(getData.dataLapPenjualanDirectory)
                            self.inputMP = str(input(systemUI.backPanel))
                            if (self.inputMP == "1"):
                                self.mpIsRunning = False
                            else:
                                print(systemUI.errorInputPanel)

                    elif (self.inputSubMenu == "2"):
                        while (self.mpIsRunning == True):                            
                            self.tempVarData = ['Nomor Transaksi', 'Tanggal Penjualan', 'Harga Beli', 'Jumlah']
                            self.tempInputData = ['','','','']
                            
                            for i in range(0, len(self.tempVarData)):
                                self.tempInputData[i] = str(input("Masukkan " + self.tempVarData[i] + ": "))

                            self.tempData = {
                                'Nomor Transaksi' : [self.tempInputData[0]],
                                'Tanggal Penjualan' : [self.tempInputData[1]],
                                'Harga Beli' : [self.tempInputData[2]],
                                'Jumlah' : [self.tempInputData[3]],
                                'Total Harga' : [str(int(self.tempInputData[2])*int(self.tempInputData[3]))]
                            }

                            mp.addData(getData.dataLapPenjualanDirectory, self.tempData)
                            mp.readData(getData.dataLapPenjualanDirectory)
                            print("Data berhasil ditambahkan!")

                            self.inputMP = str(input(systemUI.backPanel))
                            if (self.inputMP == "1"):
                                self.mpIsRunning = False
                            else:
                                print(systemUI.errorInputPanel)
                    
                    elif (self.inputSubMenu == "3"):
                        while (self.mpIsRunning == True):
                            
                            mp.readData(getData.dataLapPenjualanDirectory)
                            self.inputRowDelete = int(input(systemUI.delete))
                            
                            mp.deleteData(getData.dataLapPenjualanDirectory, int(self.inputRowDelete))
                            mp.readData(getData.dataLapPenjualanDirectory)
                            print("Data berhasil dihapus!")

                            self.inputMP = str(input(systemUI.backPanel))
                            if (self.inputMP == "1"):
                                self.mpIsRunning = False
                            else:
                                print(systemUI.errorInputPanel)

                    elif (self.inputSubMenu == "4"):
                        self.subMenuIsRunning = False

                    else:
                        print(systemUI.errorInputPanel)

            elif(self.inputMainMenu == "4"):
                while (self.subMenuIsRunning == True):
                    self.mpIsRunning = True
                    self.inputSubMenu = str(input(systemUI.selectCRUD))

                    if (self.inputSubMenu == "1"):
                        while (self.mpIsRunning == True):
                            mp.readData(getData.dataStokGudangDirectory)
                            self.inputMP = str(input(systemUI.backPanel))
                            if (self.inputMP == "1"):
                                self.mpIsRunning = False
                            else:
                                print(systemUI.errorInputPanel)

                    elif (self.inputSubMenu == "2"):
                        while (self.mpIsRunning == True):                            
                            self.tempVarData = ['ID', 'Tanggal', 'Berat Stok Gudang', 'Status Stok Gudang']
                            self.tempInputData = ['','','','']
                            
                            for i in range(0, len(self.tempVarData)):
                                self.tempInputData[i] = str(input("Masukkan " + self.tempVarData[i] + ": "))

                            self.tempData = {
                                'ID' : [self.tempInputData[0]],
                                'Tanggal' : [self.tempInputData[1]],
                                'Berat Stok Gudang' : [self.tempInputData[2]],
                                'Status Stok Gudang' : [self.tempInputData[3]]
                            }

                            mp.addData(getData.dataStokGudangDirectory, self.tempData)
                            mp.readData(getData.dataStokGudangDirectory)
                            print("Data berhasil ditambahkan!")

                            self.inputMP = str(input(systemUI.backPanel))
                            if (self.inputMP == "1"):
                                self.mpIsRunning = False
                            else:
                                print(systemUI.errorInputPanel)
                    
                    elif (self.inputSubMenu == "3"):
                        while (self.mpIsRunning == True):
                            
                            mp.readData(getData.dataStokGudangDirectory)
                            self.inputRowDelete = int(input(systemUI.delete))
                            
                            mp.deleteData(getData.dataStokGudangDirectory, int(self.inputRowDelete))
                            mp.readData(getData.dataStokGudangDirectory)
                            print("Data berhasil dihapus!")

                            self.inputMP = str(input(systemUI.backPanel))
                            if (self.inputMP == "1"):
                                self.mpIsRunning = False
                            else:
                                print(systemUI.errorInputPanel)

                    elif (self.inputSubMenu == "4"):
                        self.subMenuIsRunning = False

                    else:
                        print(systemUI.errorInputPanel)

            elif(self.inputMainMenu == "5"):
                while (self.subMenuIsRunning == True):
                    self.mpIsRunning = True
                    self.inputSubMenu = str(input(systemUI.selectCRUD))

                    if (self.inputSubMenu == "1"):
                        while (self.mpIsRunning == True):
                            mp.readData(getData.dataStokPenyortirannDirectory)
                            self.inputMP = str(input(systemUI.backPanel))
                            if (self.inputMP == "1"):
                                self.mpIsRunning = False
                            else:
                                print(systemUI.errorInputPanel)

                    elif (self.inputSubMenu == "2"):
                        while (self.mpIsRunning == True):                            
                            self.tempVarData = ['ID', 'Tanggal', 'Berat Stok Penyortiran', 'Status Stok Penyortiran']
                            self.tempInputData = ['','','','']
                            
                            for i in range(0, len(self.tempVarData)):
                                self.tempInputData[i] = str(input("Masukkan " + self.tempVarData[i] + ": "))

                            self.tempData = {
                                'ID' : [self.tempInputData[0]],
                                'Tanggal' : [self.tempInputData[1]],
                                'Berat Stok Penyortiran' : [self.tempInputData[2]],
                                'Status Stok Penyortiran' : [self.tempInputData[3]]
                            }

                            mp.addData(getData.dataStokPenyortirannDirectory, self.tempData)
                            mp.readData(getData.dataStokPenyortirannDirectory)
                            print("Data berhasil ditambahkan!")

                            self.inputMP = str(input(systemUI.backPanel))
                            if (self.inputMP == "1"):
                                self.mpIsRunning = False
                            else:
                                print(systemUI.errorInputPanel)
                    
                    elif (self.inputSubMenu == "3"):
                        while (self.mpIsRunning == True):
                            
                            mp.readData(getData.dataStokPenyortirannDirectory)
                            self.inputRowDelete = int(input(systemUI.delete))
                            
                            mp.deleteData(getData.dataStokPenyortirannDirectory, int(self.inputRowDelete))
                            mp.readData(getData.dataStokPenyortirannDirectory)
                            print("Data berhasil dihapus!")

                            self.inputMP = str(input(systemUI.backPanel))
                            if (self.inputMP == "1"):
                                self.mpIsRunning = False
                            else:
                                print(systemUI.errorInputPanel)

                    elif (self.inputSubMenu == "4"):
                        self.subMenuIsRunning = False

                    else:
                        print(systemUI.errorInputPanel)

            elif(self.inputMainMenu == "6"):
                while (self.subMenuIsRunning == True):
                    self.mpIsRunning = True
                    self.inputSubMenu = str(input(systemUI.selectCRUD))

                    if (self.inputSubMenu == "1"):
                        while (self.mpIsRunning == True):
                            mp.readData(getData.dataStokProdukJadiDirectory)
                            self.inputMP = str(input(systemUI.backPanel))
                            if (self.inputMP == "1"):
                                self.mpIsRunning = False
                            else:
                                print(systemUI.errorInputPanel)

                    elif (self.inputSubMenu == "2"):
                        while (self.mpIsRunning == True):                            
                            self.tempVarData = ['ID', 'Tanggal', 'Merk', 'Harga Beras', 'Status Stok Beras', 'Berat Stok Beras']
                            self.tempInputData = ['','','','','','']
                            
                            for i in range(0, len(self.tempVarData)):
                                self.tempInputData[i] = str(input("Masukkan " + self.tempVarData[i] + ": "))

                            self.tempData = {
                                'ID' : [self.tempInputData[0]],
                                'Tanggal' : [self.tempInputData[1]],
                                'Merk' : [self.tempInputData[2]],
                                'Harga Beras' : [self.tempInputData[3]],
                                'Status Stok Beras' : [self.tempInputData[4]],
                                'Berat Stok Beras' : [self.tempInputData[5]]
                            }

                            mp.addData(getData.dataStokProdukJadiDirectory, self.tempData)
                            mp.readData(getData.dataStokProdukJadiDirectory)
                            print("Data berhasil ditambahkan!")

                            self.inputMP = str(input(systemUI.backPanel))
                            if (self.inputMP == "1"):
                                self.mpIsRunning = False
                            else:
                                print(systemUI.errorInputPanel)
                    
                    elif (self.inputSubMenu == "3"):
                        while (self.mpIsRunning == True):
                            
                            mp.readData(getData.dataStokProdukJadiDirectory)
                            self.inputRowDelete = int(input(systemUI.delete))
                            
                            mp.deleteData(getData.dataStokProdukJadiDirectory, int(self.inputRowDelete))
                            mp.readData(getData.dataStokProdukJadiDirectory)
                            print("Data berhasil dihapus!")

                            self.inputMP = str(input(systemUI.backPanel))
                            if (self.inputMP == "1"):
                                self.mpIsRunning = False
                            else:
                                print(systemUI.errorInputPanel)

                    elif (self.inputSubMenu == "4"):
                        self.subMenuIsRunning = False

                    else:
                        print(systemUI.errorInputPanel)

            elif(self.inputMainMenu == "7"):
                print("Terimakasih telah menggunakan aplikasi HIBER.IN!")
                self.menuIsRunning = False

            else:
                print(systemUI.errorInputPanel)
            
rs = RunSystem()
rs.run()