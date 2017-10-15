import json

danielstuff = open('./lists/peopleObjects.json', 'r')
peops = json.loads(danielstuff.read());
peops = peops['people']
for peop in peops:
    names.add(peop['person'])
    peopcomps = set([])
    for elem in peop['employment']:
        peopcomps.add(elem['name'])
    companies[peop['person']] = peopcomps
danielstuff.close()
