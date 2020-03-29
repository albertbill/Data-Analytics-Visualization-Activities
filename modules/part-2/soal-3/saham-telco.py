import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

#import dataset
data_xl = pd.read_csv("Dataset Saham/EXCL.JK.csv",
                      parse_dates=["Date"])
data_fren = pd.read_csv("Dataset Saham/FREN.JK.csv",
                        parse_dates=["Date"])
data_isat = pd.read_csv("Dataset Saham/ISAT.JK.csv",
                        parse_dates=["Date"])
data_tsel = pd.read_csv("Dataset Saham/TLKM.JK.csv",
                        parse_dates=["Date"])

# -------------------------------------Soal Nomor 1----------------------------------------
sns.set(style="darkgrid")
plt.figure("Harga Historis Saham Provider Telco Indonesia", figsize=(12, 8))
plt.plot(data_xl["Date"], data_xl["Close"],
         color="green", label="PT XL Axiata TBK")
plt.plot(data_fren["Date"], data_fren["Close"],
         color="orange", label="PT Smartfren Teleco TBK")
plt.plot(data_isat["Date"], data_isat["Close"],
         color="blue", label="PT Indosat TBK")
plt.plot(data_tsel["Date"], data_tsel["Close"], color="red",
         label="PT Telekomunikasi Indonesia TBK")
plt.xlabel("Tanggal")
plt.ylabel("Rupiah (IDR)")
plt.xticks(rotation=45)

label = ['PT XL Axiata Tbk', 'PT Smartfren Telecom Tbk',
         'PT Indosat Tbk', 'PT Telekomunikasi Indonesia Tbk']
plt.legend(label, loc='center', bbox_to_anchor=(
    0.5, 1.05), ncol=4, frameon=False)
myFmt = mdates.DateFormatter('%d-%m-%Y')
plt.subplot().xaxis.set_major_formatter(myFmt)
plt.tight_layout()
plt.show()
# -------------------------------------Soal Nomor 1----------------------------------------

# -------------------------------------Soal Nomor 2----------------------------------------
xl_apr = data_xl[(data_xl["Date"] > "2019-03-29") &
                 (data_xl["Date"] < "2019-05-01")]
fren_apr = data_fren[(data_fren["Date"] > "2019-03-29") &
                     (data_fren["Date"] < "2019-05-01")]
isat_apr = data_isat[(data_isat["Date"] > "2019-03-29") &
                     (data_isat["Date"] < "2019-05-01")]
tsel_apr = data_tsel[(data_tsel["Date"] > "2019-03-29") &
                     (data_tsel["Date"] < "2019-05-01")]

sns.set(style="darkgrid")
plt.figure(
    "Harga Historis Saham Provider Telco Indonesia (April 2019)", figsize=(12, 8))
plt.plot(xl_apr["Date"], xl_apr["Close"],
         color="green", label="PT XL Axiata TBK")
plt.plot(fren_apr["Date"], fren_apr["Close"],
         color="orange", label="PT Smartfren Teleco TBK")
plt.plot(isat_apr["Date"], isat_apr["Close"],
         color="blue", label="PT Indosat TBK")
plt.plot(tsel_apr["Date"], tsel_apr["Close"], color="red",
         label="PT Telekomunikasi Indonesia TBK")
plt.xlabel("Tanggal")
plt.ylabel("Rupiah (IDR)")
plt.xticks(rotation=45)

label = ['PT XL Axiata Tbk', 'PT Smartfren Telecom Tbk',
         'PT Indosat Tbk', 'PT Telekomunikasi Indonesia Tbk']
plt.legend(label, loc='center', bbox_to_anchor=(
    0.5, 1.05), ncol=4, frameon=False)
myFmt = mdates.DateFormatter('%d-%m-%Y')
plt.subplot().xaxis.set_major_formatter(myFmt)
plt.tight_layout()
plt.show()
