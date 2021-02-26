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
writer(intersections+'\n')
for i,j in g.gdict.items():
    writer(str(i+'\n'))
    writer(str(len(j))+'\n')
    if len(j)>1:
        for i in j:
            writer(str(list(i.values())[0])+" ")
            writer(str(int(i['weight'])*2)+'\n')

    else:
        for i in j:
            writer(str(list(i.values())[0])+" ")
            writer(str(i['weight'])+'\n')

