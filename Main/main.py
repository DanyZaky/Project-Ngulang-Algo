import pandas as pd

class Manipulation():
    def addData(fileName):
        data = {
            'Nama' : ['Sisca Cahya Puspita'],
            'Nim' : ['1924101030009'],
            'IPK' : ['3.90']
        }
        df = pd.DataFrame(data)
        df.to_csv(fileName, mode='a', index=False, header=False)

    def deleteData(fileName):
        df = pd.read_csv(fileName)
        df = df.drop(index=2)
        df.to_csv(fileName, encoding='utf-8', index=False)

    def readData(fileName):
        df = pd.read_csv(fileName)
        print(df)

Manipulation.deleteData('C:/Users/TUF GAMING/Downloads/data.csv')
#ReadData('C:/Users/TUF GAMING/Downloads/data.csv')