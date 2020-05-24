import pandas as pd

df = pd.read_csv(
    "hrdata.csv",
    index_col="Employee",
    parse_dates=["Hired"],
    header=0,
    names=["Employee", "Hired", "Sal", "Sick Days"],
)

print(df)

print(type(df["Hired"][0]))

df.loc["Cookie Cat"] = ["2016-07-07", "2000", "0"]
df.to_csv("hrdatamodified.csv")
