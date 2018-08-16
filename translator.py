""" Final Goal: print translated genome with its respective polypeptides """


## start and stop codons to determine ORFs
stop_codons = ['TAG', 'TAA', 'TGA']
start_codon = 'ATG'

## prints every open reading frame in genome
## print_orfs: (listof Str) -> None
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
        
## prints the open reading frames of the given genome
## translate: Str -> None 
def translate(gen_txt):
    f = open(gen_txt, 'r')
    gen_lst = f.readlines()
    f.close() 
    print_orfs(gen_lst[0])
    
translate('phi genome.txt')