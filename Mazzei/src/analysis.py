import spacy


class Analysis:
    def __init__(self, text):
        self.text = text.lower()
        self.nlp = spacy.load("en_core_web_md")
        self.doc = self.nlp(self.text)


if __name__ == "__main__":
    analysis = Analysis("This is a test")
    print(analysis.text)
    print(analysis.doc)
