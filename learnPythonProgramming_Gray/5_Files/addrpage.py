from __future__ import print_function
new_page = open("addressbook.html", "w")
print('<html>', file= new_page)
print('<head>'
        '<meta http-equiv="content-type" content="text/html"; charset=us-ascii>'
        '<title>addressbook</title></head>', file=new_page, sep="\n")
print(' <body><p>Hello world</p></body>', file=new_page, sep="\n") 
print('</html>', file=new_page)
new_page.close()
