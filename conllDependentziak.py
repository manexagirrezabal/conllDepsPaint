import depGraphDot

def readConllFile (f):
    fi = open(f, "r")
    local_lines = [line.decode("utf8").rstrip().split("\t") for line in fi]
    fi.close()
    return local_lines

def getIndependentVs (linev):
    resV=[]
    vocV=[]
    ind=0
    resV.append([])
    vocV.append({})
    
    for i in xrange(len(linev)):
        print i, linev[i], len(linev[i])
        if len(linev[i]) > 1:
            resV[ind].append([str(linev[i][0]), linev[i][1], linev[i][6], linev[i][7]])
            vocV[ind][str(linev[i][0])]=linev[i][1]
        else:
            ind=ind+1
            print resV
            resV.append([])
            vocV.append({})
    return resV, vocV

import sys
marraztekoak,hiztegiak = getIndependentVs(readConllFile(sys.argv[1]))
#print len(marraztekoak), len(hiztegiak)
for ind, i in enumerate(marraztekoak):
    print len(marraztekoak[ind]), len(hiztegiak[ind])
for ind, i in enumerate(marraztekoak):
    print marraztekoak[ind]
    depGraphDot.paint (marraztekoak[ind], hiztegiak[ind], ind)

