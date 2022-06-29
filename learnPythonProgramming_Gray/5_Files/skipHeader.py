dataSource = open('name_addr.csv', 'r')
dataSrcIter = iter(dataSource)
next(dataSrcIter)
for item in dataSrcIter:
    quotes = item.split(",")
    fields = [f.strip("\"") for f in quotes]
    print(fields[0], fields[1], fields[2], fields[4])
