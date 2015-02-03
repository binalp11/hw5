#this is exercise 2 of Chapter 4 in PFB



# open genomic_dna.txt file 
genome_dna = open('genomic_dna.txt')
genome = genome_dna.read()

#open exons.txt
exons = open('exons.txt')

#empty variable to hold coding sequence
tempseq = ''

#create and open a codingseq.txt file to output to
output = open('coding_sequence.txt', 'w')

#for loop that gets the start and stop locations and 
#extracts those from the genome and appends them to 
#the temporary sequence
for ii in exons:
    startstop = ii.split(',')
    startposition = int(startstop[0])
    endposition = int(startstop[1])
    coding_region = genome[startposition:endposition]
    tempseq = tempseq + coding_region

output.write(tempseq)
output.close()

print('Coding Sequence Generated')