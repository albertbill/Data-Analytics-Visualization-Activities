# Exercise 3 - Database *Kampus* Menggunakan MongoDB

## Membuat database menggunakan MongoDB

Mengaktifkan server **MongoDB**.
```bash
C:\Program Files\MongoDB\Server\4.2\bin>mongod
```


Menjalankan program **MongoDB**.
```bash
C:\Program Files\MongoDB\Server\4.2\bin>mongo
```


Membuat dan menggunakan database **Kampus**.
```bash
> use Kampus
switched to db Kampus
```


1. Membuat **users**
```bash
> db.createUser({
... user:"andi",
... pwd:"anditopsecret",
... roles:["readWrite","dbAdmin"]
... })
Successfully added user: { "user" : "andi", "roles" : [ "readWrite", "dbAdmin" ] }
> db.createUser({
... user:"budi",
... pwd:"buditopsecret",
... roles:["readWrite"]
... })
Successfully added user: { "user" : "budi", "roles" : [ "readWrite" ] }
```


2. Membuat collections **Dosen**
```bash
> db.createCollection("Dosen")
```

  Memasukkan data ke dalam collections **Dosen**
```bash
> db.Dosen.insertMany([
... {nama:"Caca", usia:28, asal:"Jakarta", bidang:"Fisika Astrologi", titel:"S2", status:"Honorer", nip:123, matkul:["Metrologi", "Kosmologi", "Kalkulus"]},
... {nama:"Dedi", usia:29, asal:"Yogyakarta", bidang:"Fisika Terapan", titel:"S3", status:"PNS", nip:456, matkul:["Instrumentasi", "Elektronika", "Fisika Dasar"]},
... {nama:"Euis", usia:30, asal:"Bandung", bidang:"Fisika Teoretik", titel:"S1", status:"Honorer", nip:789, matkul:["Fisika Dasar", "Fisika Modern", "Kalkulus"]}
... ])
```


3. Membuat collections **Mahasiswa**
```bash
> db.createCollection("Mahasiswa")
```

  Memasukkan data ke dalam collections **Mahasiswa**
```bash
> db.Mahasiswa.insertMany([
... {nama:"Faza", usia:19, asal:"Aceh", prodi:"Fisika", angkatan:2017, nim:123},
... {nama:"Gilang", usia:20, asal:"Semarang", prodi:"Fisika", angkatan:2017, nim:456},
... {nama:"Hanafi", usia:19, asal:"Makassar", prodi:"Fisika", angkatan:2017, nim:789}
... ])
```

## Code (Visualisasi Database *Kampus*)
```python
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
```
