import spacy
from potions_list import ingredients_list


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

    def check_for_ingredient(self):
        for token in self.doc:
            if token.text in ingredients_list:
                return token.text
        return None


if __name__ == "__main__":
    analysis = Analysis("There is knotgrass in the polyjuice potion.")
    print(analysis.text)
    print(type(analysis.text))
    print(analysis.doc)
    print(type(analysis.doc))
    print(analysis.doc[0])
    print(type(analysis.doc[0]))
    print(analysis.get_dependecy_tree())
    print(analysis.check_for_ingredient())
    # displacy.serve(analysis.doc, style="dep")
