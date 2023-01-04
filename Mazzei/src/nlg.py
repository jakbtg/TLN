import markovify
from analysis import Analysis


class NLG:
    def __init__(self, text_path):
        with open(text_path) as f:
            text = f.read()
        self.model = markovify.Text(text)

    def ask_question(self):
        question = self.model.make_sentence(tries=200)
        text = Analysis(question)
        while text.number_of_ingredients() == 0:
            question = self.model.make_sentence(tries=200)
        return question


if __name__ == "__main__":
    nlg = NLG("Mazzei/corpus/questions.txt")
    for i in range(10):
        print(nlg.ask_question())


# from simplenlg import *


# class NLG:
#     def __init__(self):
#         self.lexicon = Lexicon.getDefaultLexicon()
#         self.nlgFactory = NLGFactory(self.lexicon)
#         self.realiser = Realiser(self.lexicon)

#     # Generate a random intro
#     def generate_intro(self):
#         intro = self.nlgFactory.createClause()
#         intro.setSubject("Harry")
#         intro.setVerb("be")
#         intro.setObject("in the potions class")
#         return self.realiser.realiseSentence(intro)


# if __name__ == "__main__":
#     nlg = NLG()
#     print(nlg.generate_intro())
