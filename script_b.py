# script_a.py
import pandas as pd

# Option A: Direct variable definition

Afile = "amff.csv"
Bfile = "amfo.csv"

afuc = pd.read_csv('amff.csv')
bfuc = pd.read_csv('amfo.csv')

afuc_first = afuc.drop_duplicates(subset="Date", keep="first")
result = bfuc.merge(afuc_first, on="Date", how="left")
result["NIFTY MIDCAP 150"] = result["NIFTY MIDCAP 150"].ffill().fillna(0)

result.to_csv(Bfile, index=False)
