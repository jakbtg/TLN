import markovify
from analysis import Analysis


class NLG:
    def __init__(self, corpus):
        self.text = self.build_text_from_corpus(corpus)
        self.model = markovify.Text(self.text)
        self.model.compile(inplace=True)

    # Choose the corpus to use
    def build_text_from_corpus(self, corpus):
        if corpus == "questions":
            with open("Mazzei/corpus/questions.txt") as f:
                text = f.read()
        elif corpus == "positive answers":
            with open("Mazzei/corpus/positive_answers.txt") as f:
                text = f.read()
        elif corpus == "negative answers":
            with open("Mazzei/corpus/negative_answers.txt") as f:
                text = f.read()
        return text

    def generate_question(self):
        question = self.model.make_sentence(tries=100)
        test = Analysis(question)
        # Make sure the question contains only one ingredient
        while test.number_of_ingredients() >= 2 or test.number_of_ingredients() == 0:
            question = self.model.make_sentence(tries=100)
            test = Analysis(question)
        if question is None:
            return self.generate_question()
        return question

    def generate_answer(self):
        answer = self.model.make_sentence(tries=100)
        if answer is None:
            return self.generate_answer()
        return answer


if __name__ == "__main__":
    questions_generator = NLG("questions")
    # for i in range(20):
    #     print(questions_generator.generate_question())
    pos_answers_generator = NLG("positive answers")
    for i in range(20):
        print(pos_answers_generator.generate_answer())
    neg_answers_generator = NLG("negative answers")
    for i in range(20):
        print(neg_answers_generator.generate_answer())


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
