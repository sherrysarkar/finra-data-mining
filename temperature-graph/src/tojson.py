import json

d = {}
f = open("graph.csv", 'r')
d['size'] = int(f.readline())
nodes = f.readline().split(";")
nodedict = {}
for node in nodes:
    try:
        arr = node.split(",")
        nodedict[arr[0]] = arr[1]
    except:
        pass
d['nodes'] = nodedict
f.close()
json.dump(d, open('graph.json', 'w'))
