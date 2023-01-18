import csv


fields = ['SLNO','Name','salary','time']

rows = [  ['1','Bishesh Gurung','20,000','02:00'],
        ['2','Anmol Prasad','20,000','02:00'],
        ['3','Norbu sherpa','20,000','03:00'],
        ['4','Niten Sapkota','20,000','04:00'],

       ]

filename = "Mynewcsv.csv"

with open(filename,"w") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(fields)
    csv_writer.writerows(rows)

with open(filename,"r") as csv_file:
    csv_read = csv.reader(csv_file)

    for line in csv_read:
        print(line)