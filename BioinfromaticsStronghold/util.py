# -*- coding: utf-8 -*-
###############################################################################
# Alphabet                                                                    #
###############################################################################

class Alphabet():
    """ A minimal class for alphabets """
    def __init__(self, symbolString):
        self.symbols = symbolString
    def __len__(self):              # implements the "len" operator, e.g. "len(Alphabet('XYZ')" results in 3
        return len(self.symbols)
    def __contains__(self, sym):    # implements the "in" operator, e.g. "'A' in Alphabet('ACGT')" results in True
        return sym in self.symbols
    def __iter__(self):             # method that allows us to iterate over all symbols, e.g. "for sym in Alphabet('ACGT'): print sym" prints A, C, G and T on separate lines
        tsyms = tuple(self.symbols)
        return tsyms.__iter__()
    def __getitem__(self, ndx):
        """ Retrieve the symbol(s) at the specified index (or slice of indices) """
        return self.symbols[ndx]
    def index(self, sym):
        """ Retrieve the index of the given symbol in the alphabet. """
        return self.symbols.index(sym)
    def __str__(self):
        return self.symbols

""" Below we declare alphabet variables that are going to be available when
this module is imported """
DNA_Alphabet = Alphabet('ACGT')
RNA_Alphabet = Alphabet('ACGU')
Protein_Alphabet = Alphabet('ACDEFGHIKLMNPQRSTVWY')
Protein_wX = Alphabet('ACDEFGHIKLMNPQRSTVWYX')

def readSingleFastaFile(filename):
    seq = ""
    with open(filename,'rt') as fh:
        for line in fh:
            line = line.strip()
            if line.startswith(">"):
                continue
            seq += line
    return seq

    
