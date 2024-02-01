# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 16:56:02 2024

Sequence tools

@author: Alast
"""


seq = "atgatcatgatactactatactgagacttagatgaaatgaaacccaggtccatatgatga"

table = {
    'tca': 'S',
    'tcc': 'S',
    'tcg': 'S',
    'tct': 'S',
    'ttc': 'F',
    'ttt': 'F',
    'tta': 'L',
    'ttg': 'L',
    'tac': 'Y',
    'tat': 'Y',
    'taa': '*',
    'tag': '*',
    'tgc': 'C',
    'tgt': 'C',
    'tga': '*',
    'tgg': 'W',
    'cta': 'L',
    'ctc': 'L',
    'ctg': 'L',
    'ctt': 'L',
    'cca': 'P',
    'ccc': 'P',
    'ccg': 'P',
    'cct': 'P',
    'cac': 'H',
    'cat': 'H',
    'caa': 'Q',
    'cag': 'Q',
    'cga': 'R',
    'cgc': 'R',
    'cgg': 'R',
    'cgt': 'R',
    'ata': 'I',
    'atc': 'I',
    'att': 'I',
    'atg': 'M',
    'aca': 'T',
    'acc': 'T',
    'acg': 'T',
    'act': 'T',
    'aac': 'N',
    'aat': 'N',
    'aaa': 'K',
    'aag': 'K',
    'agc': 'S',
    'agt': 'S',
    'aga': 'R',
    'agg': 'R',
    'gta': 'V',
    'gtc': 'V',
    'gtg': 'V',
    'gtt': 'V',
    'gca': 'A',
    'gcc': 'A',
    'gcg': 'A',
    'gct': 'A',
    'gac': 'D',
    'gat': 'D',
    'gaa': 'E',
    'gag': 'E',
    'gga': 'G',
    'ggc': 'G',
    'ggg': 'G',
    'ggt': 'G' 
}

class Sequence:
    def __init__(self, seq, codon_table):
        self.seq = seq
        self.codon_table = codon_table
        self.aa_seq = []
        self.orfs = []
    
    def printSeq(self):
        print(self.seq)

    def reverse(self):
        rev = []
        seqLength = len(seq) - 1
        for idx in range(seqLength, -1, -1):
            rev.append(seq[idx])
        reverseSeq = ''.join(str(base) for base in rev)
        return reverseSeq
    
    def translate(self):
        
        def _codonise(self):
            seq_idx = 0
            codon = []
            codon_list = []
            while seq_idx < len(seq):
                if len(codon) < 3:
                    codon.append(seq[seq_idx])
                    seq_idx += 1
                else:
                    residue = ''.join(str(base) for base in codon)
                    codon_list.append(residue)
                    codon.clear()
            return codon_list
            
        codons = _codonise(seq)
        for i in codons:
            #print(i)
            self.aa_seq.append(table[i])
        return self.aa_seq
    
   
    def find_pep(self):
        pos = 0
        #pep =[]
        while self.aa_seq[pos] != '*' and pos < len(self.aa_seq) -1:
            pos += 1
            # print(self.aa_seq[pos])
        pep = self.aa_seq[:pos + 1]
        return pep


"""
Standalone method for peptides
- Returns open translation frames in list of lists
- Recursive implementation returns nested frames
- Worst performance ('MMMMMM...') is O(n2) so not great
- This method is a precursor to an ORF finder
"""
def find_pep_recursive(aa_seq, pos, arr=[]):
    start = pos
    print(start, pos)
    print("Iteration ", pos)
    while aa_seq[pos] != '*' and pos < len(aa_seq) - 1:
        pos += 1
        if aa_seq[pos] == 'M' and pos > 0:
            find_pep_recursive(aa_seq, pos, arr)
    pep = aa_seq[start:pos]
    arr.append(pep)
    return arr



# Convert sequence to list of individual residues
residues = list(seq)

mySeq = Sequence(residues, table)
aa_seq = mySeq.translate()

print(find_pep_recursive(aa_seq, 0))




#print("Variables")
#print(vars(mySeq))

#mySeq.printSeq()
#print(mySeq.reverse())
#print(mySeq.translate())