from __future__ import print_function

new_page = open('loadedBook.html', 'w')
dataSource = open('name_addr.csv', 'r')
dataSourceIter = iter(dataSource)

print('<html>',
        '  <head>',
        '    <meta http-equiv="content-type" content="text/html";',
        '      charset="us-ascii">',
        '    <title>Stooges Address Book</title>',
        '  </head>', file=new_page, sep="\n")
print('  <body>',
        '    <table>', file=new_page, sep="\n")

next(dataSourceIter)
for item in dataSourceIter:
    quotes = item.split(",")
    fields = [f.strip("\"") for f in quotes]
    print('      <tr><td>{}</td><td>{}</td><td>{}</td></tr>'.format(fields[2], fields[0], fields[4]), file=new_page)

print('    </table>',
        '  </body>',
        '</html>', file=new_page, sep="\n")
