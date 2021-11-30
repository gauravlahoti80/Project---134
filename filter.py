import csv

data = []

with open('final.csv') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        data.append(row)

headers = data[0]
planets_data = data[1:]

new_data = []

for index , row in enumerate(planets_data):
    if(row[3]!=''):
        if float(row[3]) < 100 and float(row[3]) > 0:
            new_data.append(row)
    
with open('new.csv' , 'a+' , newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(new_data)