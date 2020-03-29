import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# membuat koneksi ke database
mydb = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    database='world'
)
mycursor = mydb.cursor()

# membuat query untuk Soal 1 & 2
query1 = "SELECT Name, Population FROM country WHERE Region='Southeast Asia' ORDER BY Name"
df = pd.read_sql(query1, con=mydb)

# membuat query untuk Soal 3
query2 = "SELECT Name, GNP FROM country WHERE Region='Southeast Asia' ORDER BY Name"
df2 = pd.read_sql(query2, con=mydb)

# membuat query untuk Soal 4
query3 = "SELECT Name, SurfaceArea FROM country WHERE Region='Southeast Asia' ORDER BY Name"
df3 = pd.read_sql(query3, con=mydb)

# -------------------------------------Soal Nomor 1----------------------------------------
sns.set(style="whitegrid")
plt.figure("Populasi Negara Asean", figsize=(15, 10))
listColor = ["blue", "orange", "green", "red", "purple",
             "brown", "pink", "grey", "cyan", "magenta", "black"]
plt.bar(df["Name"], df["Population"], width=0.8, color=listColor)
plt.title("Populasi Negara ASEAN")
plt.xticks(rotation=60)
plt.xlabel("Negara")
plt.ylabel("Populasi (x100 juta jiwa)")
for i, j in enumerate(df["Population"]):
    plt.text(i-.35, j, str(j), color="black", fontsize=10)
plt.tight_layout()
plt.show()
# -----------------------------------------------------------------------------------------

# -------------------------------------Soal Nomor 2----------------------------------------
plt.figure("Populasi Negara ASEAN", figsize=(10, 8))
plt.pie(df["Population"], labels=df["Name"], autopct='%1.1f%%')
plt.axis("equal")
plt.title("Persentase Produk ASEAN")
plt.tight_layout()
plt.show()
# -----------------------------------------------------------------------------------------

# -------------------------------------Soal Nomor 3----------------------------------------
sns.set(style="whitegrid")
plt.figure("Pendapatan Bruto Nasional ASEAN", figsize=(15, 10))
plt.bar(df2["Name"], df2["GNP"], width=0.8, color=listColor)
plt.title("Pendapatan Bruto Nasional ASEAN")
plt.xticks(rotation=60)
plt.xlabel("Negara")
plt.ylabel("Gross National Product ($)")
for i, j in enumerate(df2["GNP"]):
    plt.text(i-.35, j, str(j), color="black", fontsize=10)
plt.tight_layout()
plt.show()
# -----------------------------------------------------------------------------------------

# -------------------------------------Soal Nomor 4----------------------------------------
plt.figure("Persentase Luas Daratan ASEAN")
plt.pie(df3["SurfaceArea"], labels=df3["Name"], autopct='%1.1f%%')
plt.axis("equal")
plt.tight_layout()
plt.show()
# -----------------------------------------------------------------------------------------
