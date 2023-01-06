import csv

def dataPrep(data):
    dataLs = []
    csvreader = csv.reader(data, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        dataLs.append(row)
    return dataLs

def dataSel(dataLs, select):
    grData = []
    x = []
    y = []
    for i in range(len(dataLs)):
        if dataLs[i][1] == select:
            grData.append(dataLs[i])

    for a in range(len(grData)):
        x.append(grData[a][0])
        y.append(float(grData[a][6]))

    return x, y, select
