import csv



fields = ['SLNO','Name','salary','time']

rows = [  ['1','Bishesh','20,000','02:00'],
        ['2','Anmol','20,000','02:00'],
        ['3','Norbu','20,000','03:00'],
        ['4','Niten','20,000','04:00'],

       ]

file_name = "Infosys.csv"

#Opening a csv file:
with open(file_name,"w") as csv_file:
    

#Opening write function in our csv function    
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(fields)
    csv_writer.writerows(rows)

with open(file_name,"r") as csv_file:
        csv_read = csv.reader(csv_file)

        for line in csv_read:
            print(line)
