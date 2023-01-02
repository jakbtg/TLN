import spacy
from spacy import displacy


class Analysis:
    def __init__(self, text):
        self.text = text.lower()
        self.nlp = spacy.load("en_core_web_md")
        self.doc = self.nlp(self.text)


if __name__ == "__main__":
    analysis = Analysis("This is a test")
    print(analysis.text)
    print(type(analysis.text))
    print(analysis.doc)
    print(type(analysis.doc))
    print(analysis.doc[0])
    print(type(analysis.doc[0]))
    print(analysis.doc.to_json())
    displacy.serve(analysis.doc, style="dep", port=8080)
