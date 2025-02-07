import  sys
import pandas as pd 
import matplotlib.pyplot as plt
from pathlib import Path

print("\n""\n")
print(f"System version = {sys.version.split()[0]}")
print(f"{sys.version=}".split()[0])

data = {
    "name": ["Erik", "Anna","Johan","Lisa", "Oskar"],
    "age": [28,32,40,25,50],
    "city": ["Stockholm","Göteborg","Malmö","Uppsala", "Lund"],
    "salary_sek": [45000,32000,20000,25000,30000] 
}

df = pd.DataFrame(data)

fig,ax = plt.subplots(1)

ax.bar(x = df['name'],height=df['age'])
fig.savefig(Path(__file__).parent / "ages.png")
fig.tight_layout()

print(df.head())