# script_a.py
import pandas as pd

# Option A: Direct variable definition

Afile = "amff.csv"
Bfile = "amfo.csv"

afuc = pd.read_csv('amff.csv')
bfuc = pd.read_csv('amfo.csv')

ds1_first = ds1.drop_duplicates(subset="key", keep="first")
result = ds2.merge(ds1_first, on="key", how="left")
result["value"] = result["value"].ffill().fillna(0)

miss_a = bfir[~bfir.isin(afir)].drop_duplicates()

if not miss_a.empty:
    missing_rows = pd.DataFrame({afuc.columns[0]: miss_a.values})
    afuc = pd.concat([afuc, missing_rows], ignore_index=True)

afuc = pd.merge(afuc, bfuc, on = 'ISIN', how = 'left')
print(afuc.head())

afuc.to_excel(Afile, index=False)
