import pymongo as p
import pandas as pd
import matplotlib.pyplot as plt

myClient = p.MongoClient("mongodb://localhost:27017/")

myDb = myClient["Kampus"]
colDosen = myDb["Dosen"]
colMhs = myDb["Mahasiswa"]

dataDosen = pd.DataFrame(list(colDosen.find()))
dataMhs = pd.DataFrame(list(colMhs.find()))

plt.bar(dataDosen["nama"], dataDosen["usia"], color="blue")
plt.bar(dataMhs["nama"], dataMhs["usia"], color="orange")
plt.title("Usia Warga Kampus")
plt.legend(["Dosen", "Mahasiswa"])
plt.grid()
plt.show()
