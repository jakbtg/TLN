import spacy


class Analysis:
    def __init__(self, text):
        self.text = text.lower()
        self.nlp = spacy.load("en_core_web_sm")
        self.doc = self.nlp(self.text)
