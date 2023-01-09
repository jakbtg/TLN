import markovify
from analysis import Analysis


class NLG:
    def __init__(self, corpus):
        self.model = self.build_model_from_corpus(corpus)
        self.model.compile(inplace=True)

    # Choose the corpus to use and build the model
    def build_model_from_corpus(self, corpus):
        if corpus == "questions":
            with open("Mazzei/corpus/questions.txt") as f:
                text = f.read()
                model = markovify.Text(text)
        elif corpus == "positive answers":
            with open("Mazzei/corpus/positive_answers.txt") as f:
                text = f.read()
                model = markovify.Text(text)
        elif corpus == "negative answers":
            with open("Mazzei/corpus/negative_answers.txt") as f:
                text = f.read()
                model = markovify.Text(text)
        return model

    # Generate a random question
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

    # Generate a random answer
    def generate_answer(self):
        answer = self.model.make_sentence(tries=100)
        if answer is None:
            return self.generate_answer()
        return answer


if __name__ == "__main__":
    questions_generator = NLG("questions")
    for i in range(20):
        print(questions_generator.generate_question())
    pos_answers_generator = NLG("positive answers")
    for i in range(20):
        print(pos_answers_generator.generate_answer())
    neg_answers_generator = NLG("negative answers")
    for i in range(20):
        print(neg_answers_generator.generate_answer())
