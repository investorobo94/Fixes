# script_a.py
import pandas as pd

# Option A: Direct variable definition

Afile = "trial.xlsx"
Bfile = "amf.xlsx"

afuc = pd.read_excel('trial.xlsx')
bfuc = pd.read_excel('amf.xlsx')

afir = afuc.iloc[:,0]
bfir = afuc.iloc[;,0]

miss_a = bfir - afir

new_col = pd.concat([afir,miss_a])

afir.iloc[:,0] = new_col

afir = pd.merge(afir, bfir, on = 'ISIN', how = 'left')
print(afir.head())

afir.to_excel(Afile, index=False)
