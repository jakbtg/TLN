import spacy
from spacy import displacy


class Analysis:
    def __init__(self, text):
        self.text = text.lower()
        self.nlp = spacy.load("en_core_web_md")
        self.doc = self.nlp(self.text)

    def get_dependecy_tree(self):
        dict = {}
        for token in self.doc:
            dict[token.text] = token.dep_, token.pos_, token.head.text
        return dict


if __name__ == "__main__":
    analysis = Analysis("This is a test")
    print(analysis.text)
    print(type(analysis.text))
    print(analysis.doc)
    print(type(analysis.doc))
    print(analysis.doc[0])
    print(type(analysis.doc[0]))
    print(analysis.get_dependecy_tree())
