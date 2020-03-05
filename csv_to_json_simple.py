import csv
import json

csvfile = open('C:\\Users\\file.csv', 'r')
jsonfile = open('C:\\Users\\file.json', 'w')

data = {}

fieldnames = ("MOD_NAME","RES_NAME","COL_NAME","SOURCE_DT","POS","LONGC","SCALEC","COL_MANDATORY")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    resname = row["RES_NAME"]  
    data[resname] = row
    
print(data)
#json.dump(data, jsonfile)
#out = json.dumps([row for row in reader ] )
#jsonfile.write(out)
#jsonfile.write('\n')
for row in reader:
    out = json.dump(row)
    jsonfile.write(out)
    jsonfile.write('\n')
