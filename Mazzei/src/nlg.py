# Class that generates the text with simpleNLG

from simplenlg import *


class NLG:
    def __init__(self):
        self.lexicon = Lexicon.getDefaultLexicon()
        self.nlgFactory = NLGFactory(self.lexicon)
        self.realiser = Realiser(self.lexicon)

    # Generate a random intro
    def generate_intro(self):
        intro = self.nlgFactory.createClause()
        intro.setSubject("Harry")
        intro.setVerb("be")
        intro.setObject("in the potions class")
        return self.realiser.realiseSentence(intro)


if __name__ == "__main__":
    nlg = NLG()
    print(nlg.generate_intro())
