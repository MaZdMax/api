import requests
import json

def datav2(url):
    result = requests.get(url)
    resultat= json.dumps(result.json(), indent=4)
    with open("dataapi.json", "w") as outfile:
        outfile.write(resultat)
    
    return result

print(datav2("https://api.weatherstack.com/current?query=Paris"))