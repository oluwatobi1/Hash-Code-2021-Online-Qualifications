#FOr testing the  output format and result 
#printing out on the console
from read import reader, writer
from graph import Graph

# reads the file content into var a
a = reader()
# gets street count from first line through indexing
street_count = int(a[0].split(' ')[2])
# graph problem -=- graph class
g = Graph()
for i in range(1, street_count): 
    # get an/the/current individual street
    street_line = a[i][:-1].split(' ')
    # print(street_line)    
    # nodes/edges of the graph
    start_street = street_line[0]
    end_street = street_line[1]
    #add to the graph data struct to in form of a 
    name = street_line[2]
    weight = street_line[3]
    # populates the graph 
    g.AddEdge((end_street, {start_street:name, 'weight':weight}))


# gets the intersection
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
       