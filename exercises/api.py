import pandas as pd
import requests

url = "https://restcountries.com/v3.1/all"

response = requests.get(url)

if response.status_code == 200:
    countries = response.json() # omvandlar JSON-svaret till en python lista
    data = []
    for country in countries:
        name = country.get("name",{}).get("common","Okänt")
        capital = country.get("capital",["Ingen huvudstad"])[0]
        population = country.get("population","Okänd")
        data.append([name,capital,population])
        
    df = pd.DataFrame(data,columns=["Land,","Huvudstad","Befolkning"])
    print(df.head(10))
else:
    print("Fel vid hämtning av data. ")    
    
    