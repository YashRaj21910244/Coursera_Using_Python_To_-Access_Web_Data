import urllib.request as ur
import json

url = input("Enter location: ")
print("Retrieving ",url)
data = ur.urlopen(url).read().decode()
print('Retrieved', len(data), 'characters')
List = json.loads(data)

add = 0
count = 0
for comment in List["comments"]:
    add = add + int(comment["count"])
    count = count + 1
print('Count:', count)
print('Sum:', add)
