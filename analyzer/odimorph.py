import fstinter
import math

def get_cost(aml):
    analysis, morphs, lemma = aml
    c = 0
    if 'V' in morphs:
        c += 1
    c += len(lemma)
    return c

class OdiMorph:
    def __init__(self, fstpath):
        self.fst = fstinter.FST(fstpath, get_cost)

    def lemmas(self, tokens):
        return [l for (w, (p, l)) in self.fst.analyses(tokens)]

    def analyses(self, tokens):
        return [p for (w, (p, l)) in self.fst.analyses(tokens)]