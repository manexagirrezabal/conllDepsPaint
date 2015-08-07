# -*- coding: utf-8 -*-
from lxml import etree
import sys
import string
import os

import depGraphDot

#fold="/home/magirrezaba008/puntuak/"

#ateraDenak funtzioak dependentziak barne dituen bertsoen corpusetik puntuak erauzi eta hauen dependentzia zuhaitzak marrazten ditu, pydot liburutegia erabilita. Irudiak fold aldagai orokorrean zehaztutako karpetan gordetzen dira, puntuaX.png izenpean.

def deleteStuff (folder):
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception, e:
            print e
    

def ateraDenak (filename):
    fold="/home/magirrezaba008/puntuak/"
    tree = etree.parse(filename, parser=None, base_url=None).getroot()

    for bertsoaldi in tree:
        for stanza in bertsoaldi.find('Transkripzioa').findall('stanza'):
            name = bertsoaldi.attrib['trzenb']+"_"+stanza.attrib['bertsoZenbakia']
            #deleteStuff(fold)
            zuhaitzaAtera(stanza, name)
            #for python version < 3
            #raw_input("Press Enter to continue...")
            #for python version = 3
            #input("Press Enter to continue...")
            #sys.stdin.readline()

def zuhaitzaAtera (stanza, name):
    for puntuInd, puntu in enumerate(stanza):
        puntua = puntu.findall("./l/w")
        marrazteko={}
        hiztegi={}
        for hitz in puntua:
            wid=hitz.attrib['wid']
            word=hitz.text
            parent=hitz.attrib['parent']
            parentrel=hitz.attrib['parentrel']
            try:
                marrazteko[str(parent)].append((wid, word, parentrel, parent))
            except KeyError:
                marrazteko[str(parent)]=[]
                marrazteko[str(parent)].append((wid, word, parentrel, parent))
            hiztegi[wid]=word
        print ' '.join([hitz.text for hitz in puntua])
        depGraphDot.paint(marrazteko, hiztegi, name+"_"+str(puntuInd))

def main():
    
    ateraDenak(sys.argv[1])

if __name__ == '__main__':main()


