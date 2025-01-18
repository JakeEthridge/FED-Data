from urllib.request import Request, urlopen

req = Request(
    url='https://www.federalreserve.gov/', 
    headers={'User-Agent': 'Mozilla/5.0'}
)

webpage = urlopen(req)
data = webpage.read()
print(data)

print(type(data))