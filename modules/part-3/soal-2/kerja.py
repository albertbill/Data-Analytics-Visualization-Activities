import pandas as pd

#import dataset
df_profesi = pd.read_csv("Dataset Kerja/profesi.csv", delimiter="|")

# -------------------------------------Soal Nomor 1----------------------------------------
profesi = df_profesi["occupation"].unique()
print(profesi)
print(len(profesi))
# -----------------------------------------------------------------------------------------

# -------------------------------------Soal Nomor 2----------------------------------------
df2 = df_profesi.groupby(
    [df_profesi["occupation"], df_profesi["gender"]]).describe()
df2 = df2["age"][["max", "min", "mean"]]
df2.rename(columns={"max": "max_usia", "min": "min_usia",
                    "mean": "rerata_usia"}, inplace=True)
print(df2)
# -----------------------------------------------------------------------------------------

# -------------------------------------Soal Nomor 3----------------------------------------
def persentase(x):
    return (x/x.sum())

df3 = pd.crosstab(df_profesi["occupation"],
                  df_profesi["gender"]).apply(persentase, axis=1) * 100
df3["total"] = df3["F"]+df3["M"]
df3.rename(columns={"F": "%female", "M": "%male",
                    "total": "%total"}, inplace=True)
df3 = df3[["%female", "%male", "%total"]]
print(df3)
# -----------------------------------------------------------------------------------------
