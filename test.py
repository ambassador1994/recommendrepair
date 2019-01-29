import csv

with open("data.csv", "r") as f:
    csvObj = csv.reader(f)
    data = [row for row in csvObj]
    # print(f.read())
print(data)