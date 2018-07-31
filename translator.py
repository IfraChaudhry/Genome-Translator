## Final purpose: translates a given genome into its
##     respective polypeptide   


## try out the os module here at some point 
f = open('phi genome.txt', 'r')
phi_genome = f.readlines()
f.close()

## start and stop codons to determine ORFs
stop_codons = ['TAG', 'TAA', 'TGA']
start_codon = 'ATG'


def print_orfs(genome):
    pos = 0
    orf_len = 0
    orf_sequence = ''    
    while (pos < len(genome)-2):
        codon = genome[pos:pos+3]
        if (codon in stop_codons):
            if orf_len > 100:
                print('') #blank line for organization
                print('>a_long_orf') # FASTA header
                print(orf_sequence)
            orf_len = 0 # reset length
            orf_sequence = ''
        else:
            orf_sequence += codon
            orf_len += 3
        pos += 3
        
print_orfs(phi_genome[0])