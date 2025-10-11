import csv

FILENAME= "data.csv"
DATADIR = "../../data/"
with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    for line in reader:
        print (line)  # print data as a list and inner is strings
