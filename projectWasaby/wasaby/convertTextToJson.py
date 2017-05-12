import csv
import json
import os

#convert txt to csv
filein = open('../resources/ndbc_listing.txt','r')
fileout = open('../resources/temp.txt','w')

for line in filein:
    a = line.replace('Lat','').replace('.nc', '').replace('_spectrum', '')
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
jsonfile = open('../resources/res.json','w')

fieldnames=['type','year','month','id','start','end','lat','lon']

reader = csv.DictReader(csvfile,fieldnames)
json.dump([row for row in reader],jsonfile)