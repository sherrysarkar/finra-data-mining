import json
from pathlib import Path
import copy
import re
import string

punc = re.compile('[{}]'.format(re.escape(string.punctuation)))

names = set([])
companies = {}

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
path = Path('/home/shyamal/data/opinions-all/')
relevant = open('revelant.txt', 'w')
caseLinks = open('caseLinks.txt', 'w')

counter = 0
total = 0
for g in path.iterdir():
    for f in g.iterdir():
        counter += 1
        r = f.open('r')
        data = json.loads(r.read())
        r.close()
        s = data['plain_text']
        data['plain_text'] = re.sub('\s+',' ',data['plain_text'])
        data['plain_text'] = data['plain_text'].strip()
        text_words = data['plain_text'].split(" ");
        properNouns = []
        names_found = []
        cur = ""
        for word in text_words:
            if len(word) > 0 and (word[0].isupper() or word.istitle()) and re.search(punc, word) == None:
                if cur == "":
                    cur = word.title()
                else:
                    cur += " " + word.title()
                properNouns.append(cur)
                if cur in names:
                    names_found.append(cur)
            else:
                cur = ""
        found = False
        if len(names_found) != 0:
            for noun in properNouns:
                for name in names_found:
                    if noun in companies[name]:
                        found = True
                        relevant.write(f.name)
                        relevant.write("\n")
                        caseLinks.write(f.name)
                        caseLinks.write(",")
                        caseLinks.write(name)
                        caseLinks.write(",")
                        caseLinks.write(noun)
                        caseLinks.write("\n")
                        total += 1
                        break;
                if found:
                    break
        if (counter % 1000 == 0):
            relevant.flush();
            caseLinks.flush();
            print(total)

caseLinks.close()
relevant.close()
