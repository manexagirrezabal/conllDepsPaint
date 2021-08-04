import depGraphDot

def readConllFile (f):
    fi = open(f, "r")
    local_lines = [line.rstrip().split("\t") for line in fi]
    fi.close()
    return local_lines

def getIndependentVs (linev):
    resV=[]
    vocV=[]
    ind=0
    resV.append([])
    vocV.append({})
    
    for i in range(len(linev)):
        print (i, linev[i], len(linev[i]))
        if len(linev[i]) > 1:
            resV[ind].append([str(linev[i][0]), linev[i][1], linev[i][6], linev[i][7]])
            vocV[ind][str(linev[i][0])]=linev[i][1]
        else:
            ind=ind+1
            print (resV)
            resV.append([])
            vocV.append({})
    return resV, vocV

import sys
esaldiIndependenteak,hiztegiIndependenteak = getIndependentVs(readConllFile(sys.argv[1]))
#print len(esaldiIndependenteak), len(hiztegiIndependenteak)
for ind, i in enumerate(esaldiIndependenteak):
    print (len(esaldiIndependenteak[ind]), len(hiztegiIndependenteak[ind]))


for ind, esaldi in enumerate(esaldiIndependenteak):
    marrazteko={}
    hiztegi={}
    for hitz in esaldi:
        wid=hitz[0]
        word=hitz[1]
        parent=hitz[2]
        parentrel=hitz[3]
        try:
            marrazteko[str(parent)].append((wid, word, parentrel, parent))
        except KeyError:
            marrazteko[str(parent)]=[]
            marrazteko[str(parent)].append((wid, word, parentrel, parent))
        hiztegi[wid]=word
    if len(hiztegi)>0:
        depGraphDot.paint(marrazteko, hiztegi, "esaldi_"+str(ind))
