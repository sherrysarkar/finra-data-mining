import json

names = set([])
companies = {}

danielstuff = open('./peopleObjects.json', 'r')
peops = json.loads(danielstuff.read());
peops = peops['people']
for peop in peops:
    names.add(peop['person'])
    peopcomps = set([])
    for elem in peop['employment']:
        peopcomps.add(elem['name'])
    companies[peop['person']] = peopcomps
danielstuff.close()

f = open('peopleObjects.csv', 'w')
for key in companies.keys():
    f.write(key)
    for comp in companies[key]:
        f.write("," + comp)
    f.write("\n")
f.close()
