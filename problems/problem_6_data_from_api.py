from csv import DictWriter
import requests

url = "https://api.publicapis.org/entries"
print(f"Loading data from {url}")
response = requests.get(url)
data = response.json()

fieldnames = data['entries'][0].keys()
with open('C:\\Users\\vpatyal\\Dropbox\learn\\repos\python-foundations-3-weeks\\problems\\data\\apis2.csv', 'w', encoding='utf-8') as file:
    writer = DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data['entries'])
