# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 16:56:02 2024

Sequence tools

@author: Alast
"""

class Sequence:
    def __init__(self, seq):
        self.seq = seq
    
    def printSeq(self):
        print(self.seq)
    
    def translate(self):
        seq_idx = 0
        codon = []
        translation = []
        while seq_idx < len(seq):
            if len(codon) < 3:
                codon.append(seq[seq_idx])
            else:
                residue = ''.join(str(base) for base in codon)
                translation.append(residue)
                codon.clear()
            seq_idx += 1
        return translation
    
    def reverse(self):
        rev = []
        seqLength = len(seq) - 1
        for idx in range(seqLength, -1, -1):
            rev.append(seq[idx])
        reverseSeq = ''.join(str(base) for base in rev)
        return reverseSeq
            
        

seq = "atgatcatactagactag"
residues = list(seq)
mySeq = Sequence(residues)
#mySeq.printSeq()
print(mySeq.reverse())
print(mySeq.translate())
