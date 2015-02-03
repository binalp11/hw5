#this is the first exercise of chapter 4 in PFB

#opens the input text into a object
dna = open('input.txt')

#each item in dna will run through the for loop 
for ii in dna:

    #removes the first 14 characters of each line
    withoutseqadapt = ii[14:]

    #sends new sequence to the output file named shortseq
    shortseq.write(withoutseqadapt)

    #prints the sequence length for each
    print("sequence length is " + str(len(withoutseqadapt)))

 #close file
 shortseq.close()   