from importlib.metadata import version
import sys

pandas_version = version('pandas')
print(f"pandas == {pandas_version}")

matplotlib_version = version('matplotlib')
print(f"matplotlib == {matplotlib_version}")

PythonVersion = sys.version.split(" ")[0]
print(f"Python version: {PythonVersion}")

import pandas as pd

df = pd.read_csv("athlete_events.csv")

print(df.head())

import matplotlib.pyplot as plt

df['Year'].value_counts().sort_index().plot(kind= "bar",label= "Number of athletes ",legend= True)
plt.title("Antal athleter per år")
plt.xlabel("ÅR")
plt.ylabel("Antal")
plt.savefig('/app/src/plot.png')
plt.show()
