import pydot
import os.path

def paint(marrazteko, hiztegi, name):
    INITIALVALUE=str("0")
    print ("Goazen marraztera", marrazteko)
    fold="./"
    writefilename=fold+name+'.png'
    if not os.path.isfile(writefilename):
        graph = pydot.Dot(graph_type='graph')
        unekoGuraso=INITIALVALUE
        bisitatzeko=marrazteko[unekoGuraso]
        hurrengoNodoak=[]
        while (bisitatzeko != []):
            unekoEl = bisitatzeko.pop()
            print (unekoEl)
            if unekoEl[0] in marrazteko:
                bisitatzeko = bisitatzeko + marrazteko[unekoEl[0]]

            if unekoEl[3]==INITIALVALUE: #Erroa da
                gurasoHitza = "ERROA"
                rel = "ERRO"
            else:
                gurasoHitza = hiztegi[str(unekoEl[3])]
                rel = unekoEl[2]
            unekoElHitza = unekoEl[1]
            if gurasoHitza == '"':
                gurasoHitza = 'KOMATXOAK'
            if unekoElHitza == '"':
                unekoElHitza = 'KOMATXOAK'
            edge = pydot.Edge('"'+gurasoHitza+'"', '"'+unekoElHitza+'"', label='"'+rel+'"')
            graph.add_edge(edge)
        print ("Write graph into file "+fold+name+".png")
        graph.write_png(writefilename)
    else:
        print ("Jump graph file "+fold+name+".png")

