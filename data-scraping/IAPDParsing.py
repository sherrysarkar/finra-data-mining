import json
import re
import string
from pathlib import Path
import xml.etree.ElementTree as ET

badFirmStrings = [' llc', ' lp', ' inc']
punct = re.compile('[{}]'.format(re.escape(string.punctuation)))

def normalizeName(aName):
    aName = aName.lower()
    match = re.search(punct, aName)
    if match is not None:
        aName = aName[:match.start()]

    for bad in badFirmStrings:
        aName = aName.replace(bad, '')

    aName = aName.strip()

    if aName.replace(' ', '').isalpha():
        return aName.
    else:
        return ''

secFirms = ET.parse('../data/IAPD/IA_FIRM_SEC_Feed_10_11_2017.xml').getroot()[0]
stateFirms = ET.parse('../data/IAPD/IA_FIRM_STATE_Feed_10_11_2017.xml').getroot()[0]
firmsList = []

maxLen = 0

for firm in secFirms:
    name = normalizeName(firm.find('Info').get('BusNm'))
    if len(name) > 2:
        firmsList.append(name)

        maxLen = max(maxLen, len(name))

for firm in stateFirms:
    name = normalizeName(firm.find('Info').get('BusNm'))
    if len(name) > 2:
        firmsList.append(name)

        maxLen = max(maxLen, len(name))

print('There are {} SEC firms'.format(len(firmsList)))
print('Max name length is {}'.format(maxLen))


json.dump({'firms': firmsList}, Path('../data/lists/firmsList.json').open('w'))

