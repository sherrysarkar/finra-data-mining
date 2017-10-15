import json

f = open('graph.json', 'r')
d = json.load(f)

d['nodes'] = {item[0]: item[1] for item in sorted(d['nodes'].items(), key=lambda x: int(x[1]))[-30:-1]}
d['size'] = 30

json.dump(d, open('graph2.json', 'w'))
