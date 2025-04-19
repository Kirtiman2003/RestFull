import requests

url="https://bit.ly/rawir"
lines= requests.get(url).text.split('\n')
for line in lines:
    print(line)
