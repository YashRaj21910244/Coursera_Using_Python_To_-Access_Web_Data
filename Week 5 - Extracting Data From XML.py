import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url= input('Enter location :')

x = urllib.request.urlopen(url)
data = x.read()  # read data

tree = ET.fromstring(data)

print('Retrieving ',url)
lst = tree.findall('comments/comment/count')
print('Count :',len(lst))  # print count for comment

counts = tree.findall('.//count')
x = 0
add = 0
for count in counts:
    x = int(count.text)
    add = add + x
    x = 0

print('Sum :',add)
