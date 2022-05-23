import pandas as pd
import csv
df=pd.read_csv("cleaning.csv")
print(df.shape)
del df["pl_orbper"]
del df["hyperlink"]
del df["pl_letter"]

print(df.shape)
df=df.rename({"pl_hostname":"manisha_solar_system"},axis='columns')
df.to_csv("main.csv")

