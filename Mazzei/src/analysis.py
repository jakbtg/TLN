import spacy
from potions_list import ingredients_list
from pprint import pprint


class Analysis:
    def __init__(self, text):
        self.text = text.lower()
        self.nlp = spacy.load("en_core_web_md")
        self.doc = self.nlp(self.text)
        self.positivity = self.check_positivity()

    def get_dependecies(self):
        dict = {}
        for token in self.doc:
            dict[token.text] = token.dep_, token.pos_, token.head.text
        return dict

    def check_for_ingredient(self):
        for token in self.doc:
            if token.text in ingredients_list:
                return token.text
        return None

    def check_positivity(self):
        self.positivity = True
        for token in self.doc:
            if "Neg" in token.morph.get("Polarity"):
                self.positivity = False
        return self.positivity


if __name__ == "__main__":
    analysis = Analysis("There is knotgrass in the polyjuice potion.")
    print(analysis.text)
    pprint(analysis.doc.to_json())
    print(analysis.get_dependecies())
    print(analysis.check_for_ingredient())
    print(analysis.check_positivity())
    # displacy.serve(analysis.doc, style="dep")
