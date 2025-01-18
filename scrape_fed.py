from urllib.request import Request, urlopen
import re

# Request Object
req = Request(
    url='https://www.federalreserve.gov/newsevents/pressreleases/monetary20241218a.htm', 
    headers={'User-Agent': 'Mozilla/5.0'},
    method = 'GET'
)

# Open URL
webpage = urlopen(req)
# Read HTML
data = webpage.read()
# Convert to String
html_content = data.decode('utf-8')
print('\033[1;92m' + html_content)

# Title Of Article
title_index = html_content.find('<title>')
start_index = title_index + len('<title>')
end_index = html_content.find('</title>')
print('# ' + '=' * 78 + ' #')
print(html_content[start_index:end_index])
print('# ' + '=' * 78 + ' #')

list = re.findall('<p>.*</p>', html_content, re.IGNORECASE)
fed_speak = ""

for i in list: 
    i = i.replace('<p>', '')
    i = i.replace('</p>', '')
    fed_speak += i

print(fed_speak)

