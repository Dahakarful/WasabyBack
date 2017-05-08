import csv
import json
import os

#convert txt to csv
filein = open('../resources/ndbc_listing.txt','r')
os.remove('../resources/temp.txt')
fileout = open('../resources/temp.txt','w')

for line in filein:
    a = line.replace('Lat','')
    b = a.replace('Lon','')
    c= b.replace('/',',')
    d = c.replace('_',',')
    e = d.replace(',,',',')
    f = e.replace('.','', 1)
    g = f.replace(',','', 1)
    if(g[4]==','):
        h=g.replace(',','', 1)
        fileout.write(h)
    else:
        fileout.write(g)
    print(g)
filein.close()
fileout.close()

#convert csv to json
csvfile = open('../resources/temp.txt','r')
os.remove('../resources/result.json')
jsonfile = open('../resources/result.json','w')

fieldnames=['type','year','month','id','start','end','lat','lon','extension']

reader = csv.DictReader(csvfile,fieldnames)
json.dump([row for row in reader],jsonfile)