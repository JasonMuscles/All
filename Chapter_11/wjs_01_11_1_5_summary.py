import json
import requests

url = "http://datachart.500.com/plw/history/history.shtml"

data = requests.get(url)

print(data.text)
