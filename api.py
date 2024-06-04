import requests
import json

def datav2(url):
    result = requests.get(url)
    resultat= json.dumps(result.json(), indent=4)
    with open("dataapi.json", "w") as outfile:
        outfile.write(resultat)
    
    return result

print(datav2("https://api.nasa.gov/planetary/apod?api_key=tx4JklxXQcy5YJyrpbS3wuGQnN8NxWnjkmSUAivW"))
