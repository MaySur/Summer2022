import sys
import requests
import json

if len(sys.argv) != 2:
    sys.exit()

res = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term="+sys.argv[1])

#print(json.dumps(res.json(),indent=2))

o = res.json()

for i in o["results"]:
    print(i["trackName"])
