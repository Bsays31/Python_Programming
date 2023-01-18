import csv

fields = ["SLNO.","Name","Age","State"]

rows = [["1","Bishesh Gurung","22","West Bengal"],
    ["2","Niten Sapkota","22","West Bengal"],
    ["3","Akhil Pradhan","23","West Bengal"],
    ["4","Mojesh Gurung","23","West Bengal"],
    ["5","Amit Chettri","23","West Bengal"],
    ["6","Reshab Giri","24","West Bengal"]]


with open("Amazon.csv","w") as csv_file:
    csv_write = csv.writer(csv_file)
    csv_write.writerow(fields)
    csv_write.writerows(rows)


with open("Amazon.csv","r") as csv_file:
    csv_read = csv.reader(csv_file)

    for i in csv_read:
        print(i)