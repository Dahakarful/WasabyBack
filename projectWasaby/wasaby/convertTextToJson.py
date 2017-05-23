import csv
import json
import os

# convert txt to csv
filein = open('../resources/ndbc_listing.txt','r')
fileout = open('../resources/temp.txt','w')

for line in filein:
    a = line.replace('_', ',').replace('./', '').replace('/', ',').replace('Lat', '').replace('Lon', '').replace('.nc', '')
    b = a.replace('spectrum', '').replace('sensor', '').replace(',,', ',').replace(' ', '')
    g = b.replace('ocean,temperature', 'ocean temperature').replace('air,temperature', 'air temperature')
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
print('Done!')