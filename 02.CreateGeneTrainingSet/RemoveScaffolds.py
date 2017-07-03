from sys import argv
import os


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



def ListReader(ListofScaftoRemove):
    ListToRemove = []
    with open(ListofScaftoRemove, 'r') as f:
        for line in f:
            Clean = line.strip("\n").split('\t')
            if Clean[0] not in ListToRemove:
                ListToRemove.append(Clean[0])
    return ListToRemove



def RemoveScafs(arg1, list1):
    """TODO: Docstring for RemoveScafs.

    :arg1: TODO
    :returns: TODO

    """
    def WriteDict(ModifiedDict):
        """TODO: Docstring for WriteDict.

        :ModifiedDict: TODO
        :returns: TODO

        """
        NewDictName = str(argv[1]).replace(".fasta", "_Modified.fasta")
        try:
            os.remove(NewDictName)
        except OSError:
            pass


        with open(NewDictName, 'a') as K:
            for key, value in ModifiedDict.iteritems():
                K.write(key)
                K.write("\n")
                K.write(value)
                K.write("\n")


    for item in list1:
        del arg1[item]
    WriteDict(arg1)




ReadGenome = GenomeReader(argv[1])
ReadList = ListReader(argv[2])
RemoveScafs(ReadGenome,ReadList)











