import csv
import json


fileWriteDir = "tinkersConstructMaterials.csv"

fieldNames = [
    "material",
    "level",
    "speed",
    "damage",
    "modifier",
    "durability",
    "traits",
    "part"
]


handlesFile = open("tinkersHandles.json")
headFile = open("tinkersHead.json")
extrasFile = open("tinkersExtras.json")


handles = json.load(handlesFile)
head = json.load(headFile)
extras = json.load(extrasFile)

data = {} 

dataPos = 0


for i in extras:
    data[dataPos] = ({k.lower():v for k, v in i.items()})
    data[dataPos]["part"] = "extra"
    dataPos += 1

for i in head:
    data[dataPos] = ({k.lower():v for k, v in i.items()})
    data[dataPos]["part"] = "head"
    dataPos += 1

for i in handles:
    data[dataPos] = ({k.lower():v for k, v in i.items()})
    data[dataPos]["part"] = "handles"
    dataPos += 1
 
handlesFile.close()
headFile.close()
extrasFile.close()

# csv write
with open(fileWriteDir, 'w', newline = '', encoding = "utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = fieldNames)
    writer.writeheader()
    for i in range(len(data)):
        writer.writerow(data[i])

