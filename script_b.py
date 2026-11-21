# script_a.py
import pandas as pd
from datetime import date, timedelta

# Option A: Direct variable definition

Afile = "amff.csv"
Bfile = "amfo.csv"

afuc = pd.read_csv('amff.csv')

start_date = date(2005, 4, 1)
end_date = date(2026, 9, 30)

date_range = [
  start_date + timedelta(days=i)
  for i in range((end_date - start_date).days + 1)
]

bfuc = pd.Dataframe({"Date": date_range})

print(f"Total dates: {len(date_range)}")
print(f"First: {date_range[0]}")
print(f"Last: {date_range[-1]}")

afuc_first = afuc.drop_duplicates(subset="Date", keep="first")
result = bfuc.merge(afuc_first, on="Date", how="left")
result["NIFTY MIDCAP 150"] = result["NIFTY MIDCAP 150"].ffill().fillna(0)

result.to_csv(Bfile, index=False)
