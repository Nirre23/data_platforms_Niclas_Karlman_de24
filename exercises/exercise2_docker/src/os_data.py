from pathlib import Path
import pandas as pd

# Skapa sökvägen till CSV-filen i src-mappen
data_path = Path(__file__).parent / "athlete_events.csv"

# Läs in CSV-filen
df = pd.read_csv(data_path)

# Visa de första 5 raderna i CSV-filen
print(df.head())

# Skriv ut information om DataFrame
print(df.info())



