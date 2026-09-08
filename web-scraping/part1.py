import requests
import pandas as pd
import json

URL = "https://archive.org/metadata/frenchenglishmed00gorduoft"

reponse = URL
response = requests.get(URL)

if response.status_code == 200:
    
    data = response.json()
    
    with open("data.jaon","w", encoding="utf-8") as file:
        json.dump(data,file,indent = 4)
        
    print("Connection fetch successfull!")
else:
    print("Failed fetching!")

data = response.json()
df = pd.DataFrame(data["files"])

print(df)
df.to_csv("data.csv", index = False)