import csv
celex = []
raw = open('emw.csv','r')
lns = raw.readlines()
for i in range(len(lns)):
	celex.append(lns[i].split(','))
print celex
