with open('./caseLinks1.txt', 'r') as f:
    data = set(tuple(line.split(',')) for line in f.read().strip().split('\n') if (len(set(line.split(',')[1:3])) > 1 and line.split(',')[2] not in ['Self', 'School', 'College', 'University', 'Retired', 'None']))

with open('./realCaseLinks1.txt', 'w') as f:
    f.write('\n'.join(','.join(stuff) for stuff in data))

print(len(data))
