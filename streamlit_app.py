import requests
from lxml.html import fromstring
import lxml.html

file1 = open('YourPath/PeopleAlsoAsk/keywords.txt', 'r')
file2 = open('YourPath/PeopleAlsoAsk/paa.txt', 'w')
Lines = file1.readlines()
header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        'Accept-Language': 'tr-tr,en;q=0.9',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
        }
for line in Lines:
        query = line.strip()
        response = requests.get(f'https://www.google.com/search?q={query}&start=0', headers=header).text
        tree = lxml.html.fromstring(response)
        node = tree.xpath('//@data-q')
        x = node[0]
        y = node[1]
        z = node[2]
        print(query)
        file2.write(query)
        file2.write(": ")
        file2.write(x)
        file2.write(" , ")
        file2.write(y)
        file2.write(" , ")
        file2.write(z)
        file2.write("\n")
file1.close()
file2.close()
