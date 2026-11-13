# script_a.py
import pandas as pd

# Option A: Direct variable definition

Afile = "trial.xlsx"
Bfile = "amf.xlsx"

afuc = pd.read_excel('trial.xlsx')
bfuc = pd.read_excel('amf.xlsx')

afir = afuc.iloc[:,0].str.strip().str.upper().dropna()
bfir = bfuc.iloc[:,0].str.strip().str.upper().dropna()

miss_a = bfir[~bfir.isin(afir)].drop_duplicates()

new_col = pd.concat([afir,miss_a], ignore_index = True)

afuc.iloc[:,0] = new_col

afuc = pd.merge(afuc, bfuc, on = 'ISIN', how = 'left')
print(afir.head())

afir.to_excel(Afile, index=False)
