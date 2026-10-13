import sys
import pandas as pd
print("arguments", sys.argv)

month = int(sys.argv[1])

df = pd.DataFrame({"day": [1,2], "number_of_passangers": [2,3]})
df["month"] = month
print(df)

df.to_parquet(f"output_{month}.parquete")
print(f"Hello pipeline, month = {month}")
