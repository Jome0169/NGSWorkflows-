import os 
import time 
from sys import argv


def GenomeReader(GenomeFile):
    """
    Arg: Takes in Genome File
    Rtrns: Returns a dictionary, Genome Scaffolds. 
    
    Keys genomic scaffold names being the
    keys - and the actual sequence being the value. 
    """
    GenomeScaffolds = {}
    with open(GenomeFile, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                NamedSeq = line.replace('>', '')
                GenomeScaffolds[NamedSeq] = ""
            else:
                GenomeScaffolds[NamedSeq] += line
        return GenomeScaffolds

def BlastFilereader(BLastfile):
    # BlastFilereader will return a list of list from a blast file with the
    #above commented 7 header feature from a BLAST table."""
    HitsNStuff = []
    with open(BLastfile, "r") as f:
        for line in f:
            if line.startswith("#"):
                pass
            else:   
                HitsNStuff.append(line.strip("\n").split('\t'))
    return HitsNStuff


ReadGenome = GenomeReader(argv[1])
ReadBlast = BlastFilereader(argv[2])



ListofKeys = []

for item in ReadGenome.keys():
    ListofKeys.append(item)


PleaseWorkDict = {}

for item in ListofKeys:
    PleaseWorkDict[item] = [0,0]

NestedList = []


for key, value in ReadGenome.iteritems():
    genomeLength = len(value)
    Newlist = [key, genomeLength]
    NestedList.append(Newlist)


for item in NestedList:
    key = item[0]
    NonKeyvalue = item[1]
    PleaseWorkDict[key][0] += NonKeyvalue


for item2 in ReadBlast:
    Keyname = item2[1]
    AlignLen = item2[3]
    PleaseWorkDict[Keyname][1] += int(AlignLen)



RemovalKeys = []

for Scaf, number in PleaseWorkDict.iteritems():
    if number[0] < number[1]:
        number.append(1)
    elif number[1] > 0:
        PercentageofScaf = float(number[1]) / float(number[0])
        if PercentageofScaf > .30:
            number.append(PercentageofScaf)
        else:
            RemovalKeys.append(Scaf)


    else:
        RemovalKeys.append(Scaf)

for dell in RemovalKeys:
    del PleaseWorkDict[dell]



NewFileName = str(argv[2]) + ".analyzed"


try:
    os.remove(NewFileName)
except OSError:
    pass

with open(NewFileName, 'a+') as f:
    f.write(" ScafName  ScafLength  HitLen  PercentageMito/Chloro" "\n")
    for key, value in PleaseWorkDict.iteritems():
        NewLine = str(key) + "\t" + str(value[0]) + "\t" + str(value[1]) + '\t' + \
        str(value[2]) + '\n'
        f.write(NewLine)









