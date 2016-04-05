import csv

file = open("userrev.csv")
c1 = csv.reader(file)
for row in c1:
    print row[0]
file.close()
