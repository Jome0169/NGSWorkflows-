from sys import argv



def GetHeaderFromConsvd(SeqFile):
    HeaderSeq = []
    with open (SeqFile, 'r') as f:
        for line in f:
            if line.startswith('>'):
                Newline = line.strip('\n').replace('>', '').split(" ")
                HeaderSeq.append(Newline[0])
                HeaderSeq.append(Newline[1])
            else:
                pass
    return set(HeaderSeq)



def GroupGff3(GffGenomeFile):
    AssemblyGroupin = []
    with open(GffGenomeFile, 'r') as z:
        Group = []
        for line in z:
            X = len(line)
            if X != 1:
                Cleanline = line.strip('\n').split('\t')
                Group.append(Cleanline)
            elif X == 1:
                AssemblyGroupin.append(Group)
                Group = []
    return AssemblyGroupin



def FindGoodGroups(Assmblys, seqset):
    HitSeq = []
    OneTrancsript = []
    for assmb in Assmblys:
        OnlyHeader = assmb[0][8].replace('ID=', '').split(';')
        RemoveId = OnlyHeader[0]
        if RemoveId in seqset:
            HitSeq.append(assmb)

    return HitSeq








