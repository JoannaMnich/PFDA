import csv

FILENAME= "data.csv"
DATADIR = "../../data/"
with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    for line in reader:
        print (line)  # print data as a list and inner is strings

"""""
# a) Convert the string that is read into an integer
with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    linecount = 0
    for line in reader:
        if not linecount: # first row ie header row
            print (f"{line}\n-------------------")
    else: # all subsequent rows
        print (line)

# Convert the string that is read into an integer

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    linecount = 0
    total = 0
    for line in reader:
        if not linecount: # first row ie header row
            pass
    else: # all subsequent rows
        total += int(line[1]) # why 1
        linecount += 1
print (f"average is {total/(linecount-1)}") # why -1 : 
                                # when calculating averages,  subtract 1 from the total count to not include header
                                # function gives error because use division by zero
"""""

# Modified code:

with open(DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    total = 0
    linecount = 0
    for line in reader:
        if not linecount:  # header
            linecount += 1  # add 1 to go to data without header
            continue       
        total += int(line[1])  # column 'age'
        linecount += 1

if linecount > 0:
    print(f"Average is {total / linecount}")
else:
    print("No data to calculate the average")


# b)  Use the quote parameter to read in the numbers as floats

with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    linecount = 0
    total = 0
    for line in reader:
        if not linecount: # first row ie header row
            pass
        else: # all subsequent rows
            total += line[1] # why 1
            linecount += 1
print (f"average is {total/(linecount-1)}") # why -1 


# Read as a Dictionary Object 
with open (DATADIR + FILENAME, "rt") as fp:
    reader = csv.DictReader(fp, delimiter="," , quoting=csv.QUOTE_NONNUMERIC)
    total = 0
    count = 0
    for line in reader:
        total += line['age']
# print (line)
    count +=1
print (f"average is {total/(count)}") # why is there no -1 this time?
   