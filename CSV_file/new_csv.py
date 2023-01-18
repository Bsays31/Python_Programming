import csv

with open ('Infosys.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for lines in csv_reader:
        print(lines)

    with open('us.csv','w') as csvss:
        fieldnames = ['SLNO','Name','Salary','time']

        csv_writer = csv.DictWriter(csvss,fieldnames=fieldnames)
        csv_writer.writeheader()
        for column in csv_reader:
            csv_writer.writerow(column)