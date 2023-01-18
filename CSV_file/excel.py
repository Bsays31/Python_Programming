import csv

fields = ["SLNO.","NAME","CLASS","FEES PAID"]

row = [["1","BISHESH GURUNG","12","DECEMBER"],
       ["2","BAISHALI GURUNG","12","NOVEMBER"],
       ["3","BIVEK GURUNG","11","NOT PAID"]]

file_name = "school.csv"

with open(file_name,"w") as csv_file:
    
    csv_written = csv.writer(csv_file)
    csv_written.writerow(fields)
    csv_written.writerows(row)