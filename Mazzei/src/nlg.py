import markovify
from potions_list import ingredients_list


class NLG:
    def __init__(self, text_path):
        with open(text_path) as f:
            text = f.read()
        self.model = markovify.Text(text)

    def ask_question(self):
        question = self.model.make_sentence(tries=200)
        while self.check_if_only_one_ingredient(question) == False:
            question = self.model.make_sentence(tries=200)
        return question

    def check_if_only_one_ingredient(self, text):
        num_ingredients = 0
        for token in text:
            if token.text in ingredients_list:
                num_ingredients += 1
        if num_ingredients == 1:
            return True
        else:
            return False


if __name__ == "__main__":
    nlg = NLG("Mazzei/corpus/questions.txt")
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
