import markovify
from analysis import Analysis
import spacy


nlp = spacy.load("en_core_web_md")

# Trying to generate a model, using spacy pos tags, that obeys sentence structure better than a naive model
# The improvement is not significant, so I kept the naive model
class POSifiedText(markovify.Text):
    def word_split(self, sentence):
        return ["::".join((word.orth_, word.pos_)) for word in nlp(sentence)]

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence


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
                # Tried to use POSifiedText, but the improvement is not significant
                # model = POSifiedText(text)
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
        question = self.model.make_sentence(max_overlap_ratio=0.9)
        if question is None:
            return self.generate_question()
        test = Analysis(question)
        # Make sure the question contains only one ingredient
        while test.number_of_ingredients() >= 2 or test.number_of_ingredients() == 0:
            question = self.model.make_sentence(max_overlap_ratio=0.9)
            test = Analysis(question)
        return question

    # Generate a random answer
    def generate_answer(self):
        answer = self.model.make_sentence(max_overlap_ratio=0.9)
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
