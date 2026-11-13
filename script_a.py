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

if not miss_a.empty:
    missing_rows = pd.DataFrame({afuc.columns[0]: miss_a.values})
    afuc = pd.concat([afuc, missing_rows], ignore_index=True)

afuc = pd.merge(afuc, bfuc, on = 'ISIN', how = 'left')
print(afuc.head())

afuc.to_excel(Afile, index=False)
