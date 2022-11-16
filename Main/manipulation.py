import pandas as pd

class Manipulation():
    def readData(self, fileName):
        df = pd.read_csv(fileName)
        print(df)
    
    def addData(self, fileName, data):
        df = pd.DataFrame(data)
        df.to_csv(fileName, mode='a', index=False, header=False)

    def deleteData(self, fileName, row):
        df = pd.read_csv(fileName)
        df = df.drop(index=row)
        df.to_csv(fileName, encoding='utf-8', index=False)

    