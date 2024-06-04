import requests
import json
import datetime
from urllib.parse import urlparse



def datav2(url):
    result = requests.get(url)
    parsed = urlparse(url)
    uri = parsed.path
    date = datetime.datetime.now()
    day = str(date.day)
    month = str(date.month)
    year = str(date.year)
    nom_ficher= uri.replace("/","_")
    payload = {
        'date' : str(date),
        'endpoint' : uri,
        'data' : result.json()
    }
    payload= json.dumps(payload, indent=4)
    
    with open(day+"-"+month+"-"+year+nom_ficher+".json", "w") as outfile:
        outfile.write(payload)
    
    return result 
  

print(datav2("https://api.nasa.gov/planetary/apod?api_key=tx4JklxXQcy5YJyrpbS3wuGQnN8NxWnjkmSUAivW"))