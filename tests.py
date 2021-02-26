#FOr testing the  output format and result 
#printing out on the console
from read import reader, writer
from graph import Graph

a = reader()
street_count = int(a[0].split(' ')[2])

g = Graph()
for i in range(1, street_count): 
    street_line = a[i][:-1].split(' ')
    # print(street_line)    
    start_street = street_line[0]
    end_street = street_line[1]
    name = street_line[2]
    weight = street_line[3]
    g.AddEdge((end_street, {start_street:name, 'weight':weight}))



intersections = str(len(g.gdict))
print(intersections)
for i,j in g.gdict.items():
    print(str(i))
    print(str(len(j)))
    if len(j)>1:
        for i in j:
            print(str(list(i.values())[0])+" "+ str(int(i['weight'])*2))
    else:
        for i in j:
            print(str(list(i.values())[0])+" "+ str(i['weight']))
       