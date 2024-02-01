# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 16:56:02 2024

Sequence tools

@author: Alast
"""

class Sequence:
    def __init__(self, seq, codon_table):
        self.seq = seq
        self.codon_table = codon_table
    
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
        aa_residues = []
        for i in codons:
            print(i)
            aa_residues.append(table[i])
        return aa_residues
    
"""    
    def orf(self, aa_residues):
        start = 0
        while aa_residues[start] != '*':
            start += 1
        return aa_residues[:start]
"""   
        

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

seq = "atgatcatactagacttagaaaaaa"
residues = list(seq)

mySeq = Sequence(residues, table)
#mySeq.printSeq()
#print(mySeq.reverse())
print(mySeq.translate())
