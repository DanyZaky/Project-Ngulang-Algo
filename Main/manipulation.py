import pandas as pd

class Manipulation():
    def readData(self, fileName):
        df = pd.read_csv(fileName)
        print(df)
    
    def addData(self, fileName):
        data = {
            'Nama' : ['Sisca Cahya Puspita'],
            'Nim' : ['1924101030009'],
            'IPK' : ['3.90']
        }
        df = pd.DataFrame(data)
        df.to_csv(fileName, mode='a', index=False, header=False)

    def deleteData(self, fileName):
        df = pd.read_csv(fileName)
        df = df.drop(index=2)
        df.to_csv(fileName, encoding='utf-8', index=False)

    