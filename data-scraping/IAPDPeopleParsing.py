import json
import re
import string
from pathlib import Path
import xml.etree.ElementTree as ET

badFirmStrings = [' llc', ' lp', ' inc']
punct = re.compile('[{}]'.format(re.escape(string.punctuation)))

def normalizeCompanyName(aName):
    if aName is None:
        return ''

    aName = aName.lower()
    match = re.search(punct, aName)
    if match is not None:
        if match.start() < len(aName) - 6:
            return ''

        aName = aName[:match.start()]

    for bad in badFirmStrings:
        aName = aName.replace(bad, '')

    aName = aName.strip()

    if aName.replace(' ', '').isalpha():
        return aName.title()
    else:
        return ''

def normalizePersonName(fName, lName):
    if not (fName.isalpha() and lName.isalpha()):
        return ''

    return fName.title() + ' ' + lName.title()



peoplePath = Path('../data/IAPD/IA_INDVL_Feed_10_11_2017/').resolve()

firmsSet = set()
peopleList = []
peopleObjList = []

maxLenFirms = 0
maxLenPeople = 0

count = 0

for peopleFile in peoplePath.iterdir():
    print('People {}'.format(count))
    count += 1
    peoples = ET.parse(str(peopleFile)).getroot()[0]

    for indiv in peoples:
        # print(indiv.getchildren())
        info = indiv.find('Info')

        name = normalizePersonName(info.get('firstNm'), info.get('lastNm'))
        if len(name) > 3:
            empsList = []

            for emp in indiv.find('EmpHss'):
                # print(emp.attrib)

                empName = normalizeCompanyName(emp.get('orgNm'))
                if len(empName) > 3:

                    try:
                        empMonth, empYear = emp.get('fromDt').split('/')

                        firmsSet.add(empName)
                        maxLenFirms = max(maxLenFirms, len(empName))

                        empsList.append({
                            'name': empName,
                            'date': int(empYear) + ((int(empMonth) - 1) / 12)
                        })

                    except:
                        pass

            if len(empsList) > 0:
                empsList = sorted(empsList, key=lambda x: x['date'])

                peopleObjList.append({
                    'person': name,
                    'employment': empsList
                })
                peopleList.append(name)
                maxLenPeople = max(maxLenPeople, len(name))



print('There are {} firms'.format(len(firmsSet)))
print('Max firm name length is {}'.format(maxLenFirms))

print('There are {} people'.format(len(peopleList)))
print('Max people name len is {}'.format(maxLenPeople))


json.dump({'firms': list(firmsSet)}, Path('../data/lists/firmsList.json').open('w'))
json.dump({'people': peopleList}, Path('../data/lists/peopleList.json').open('w'))
json.dump({'people': peopleObjList}, Path('../data/lists/peopleObjects.json').open('w'))

