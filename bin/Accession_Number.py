## Retrieve the accession  number and original sequence for a query multi-fasta file 
import sys
file = sys.argv[1]

fp1 = open(file, 'r+')
fp2 = open(file+'.txt','w+')

lines = fp1.readlines()

for line in lines:
    if len(line)>1 and line[0]=='>':
        segs=line.split('[')
        if len(segs)>1:
            nameList = segs[1].split(' ')
            genus=segs[0]
            if len(nameList[1])>=6: 
                   species=nameList[1][0:5]
            else:
                species = nameList[1]
            organism = genus + "_" + species
            if organism[-1] != '\n':
               organism = organism + '\n'
        else:
            organism= ''
        segs = segs[0].split(' ')
        gi = segs[0]
        fp2.write('>'+gi + '\n')
    else:
        if len(line)>1 and line[-2] != ']':
            fp2.write(line)
fp1.close()
fp2.close()