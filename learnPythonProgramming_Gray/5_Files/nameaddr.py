dataSource = open("name_addr.csv", "r")
for addr in dataSource:
    quotes = addr.split(",")
    fields = [f.strip("\"") for f in quotes]
    print(fields[0], fields[1], fields[2], fields[4])
dataSource.close()
