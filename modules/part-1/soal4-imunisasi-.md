# Exercise 4 - Imunisasi

## Dataset
Dataset dapat diunduh melalui: [Data Balita Terimunisasi di Indonesia BPS 1995-2017](https://www.kaggle.com/lintangwisesa/balita-terimunisasi-di-indonesia-bps-19952017)

## Code
```python
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#import dataset
data_bcg = pd.read_csv(
    "Dataset Imunisasi/Balita Terimunisasi BCG 1995-2017.csv", na_values="n.a")
data_campak = pd.read_csv(
    "Dataset Imunisasi/Balita Terimunisasi Campak 1995-2017.csv", na_values="n.a")
data_dpt = pd.read_csv(
    "Dataset Imunisasi/Balita Terimunisasi DPT 1995-2017.csv", na_values="n.a")
data_polio = pd.read_csv(
    "Dataset Imunisasi/Balita Terimunisasi Polio 1995-2017.csv", na_values="n.a")

# mengolah data yang missing
data_bcg = data_bcg.interpolate()
data_bcg["% Balita yang tidak mendapat imunisasi BCG"] = 100 - \
    data_bcg["% Balita yang pernah mendapat imunisasi BCG"]

data_campak = data_campak.interpolate()
data_campak["% Balita yang tidak mendapat imunisasi Campak"] = 100 - \
    data_campak["% Balita yang pernah mendapat imunisasi Campak"]

data_dpt = data_dpt.interpolate()
data_dpt["% Balita yang tidak mendapat imunisasi DPT"] = 100 - \
    data_dpt["% Balita yang pernah mendapat imunisasi DPT"]

data_polio = data_polio.interpolate()
data_polio["% Balita yang tidak mendapat imunisasi Polio"] = 100 - \
    data_polio["% Balita yang pernah mendapat imunisasi Polio"]

# visualisasi data balita terimunisasi
sns.set(style="whitegrid")
plt.figure('Persentasi balita terimunisasi 1995-2017', figsize=(10, 8))
plt.subplot(221)
sns.barplot(x='Tahun', y='% Balita yang pernah mendapat imunisasi BCG',
            data=data_bcg, color='red')
plt.xticks(rotation=90)
plt.ylabel('')
plt.title('BCG')

plt.subplot(222)
sns.barplot(x="Tahun", y="% Balita yang pernah mendapat imunisasi Campak",
            data=data_campak, color="green")
plt.xticks(rotation=90)
plt.ylabel("")
plt.title("Campak")

plt.subplot(223)
sns.barplot(x="Tahun", y="% Balita yang pernah mendapat imunisasi DPT",
            data=data_dpt, color="yellow")
plt.xticks(rotation=90)
plt.ylabel("")
plt.title("DPT")

plt.subplot(224)
sns.barplot(x="Tahun", y="% Balita yang pernah mendapat imunisasi Polio",
            data=data_polio, color="blue")
plt.xticks(rotation=90)
plt.ylabel("")
plt.title("Polio")
plt.tight_layout()

# visualisasi data balita tidak terimunisasi
plt.figure('Persentasi balita tidak terimunisasi 1995-2017', figsize=(10, 8))
plt.subplot(221)
sns.barplot(x='Tahun', y='% Balita yang tidak mendapat imunisasi BCG',
            data=data_bcg, color='red')
plt.xticks(rotation=90)
plt.ylabel('')
plt.title('BCG')

plt.subplot(222)
sns.barplot(x="Tahun", y="% Balita yang tidak mendapat imunisasi Campak",
            data=data_campak, color="green")
plt.xticks(rotation=90)
plt.ylabel("")
plt.title("Campak")

plt.subplot(223)
sns.barplot(x="Tahun", y="% Balita yang tidak mendapat imunisasi DPT",
            data=data_dpt, color="yellow")
plt.xticks(rotation=90)
plt.ylabel("")
plt.title("DPT")

plt.subplot(224)
sns.barplot(x="Tahun", y="% Balita yang tidak mendapat imunisasi Polio",
            data=data_polio, color="blue")
plt.xticks(rotation=90)
plt.ylabel("")
plt.title("Polio")
plt.tight_layout()

plt.show()
```
