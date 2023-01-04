import spacy
from potions_list import ingredients_list
from pprint import pprint


class Analysis:
    def __init__(self, text):
        self.text = text.lower()
        self.nlp = spacy.load("en_core_web_md")
        self.doc = self.nlp(self.text)
        self.positivity = self.check_positivity()

    # Get the dependencies of the text in the form:
    # {token: (dependency, part of speech, head)}
    def get_dependecies(self):
        dict = {}
        for token in self.doc:
            dict[token.text] = token.dep_, token.pos_, token.head.text
        return dict

    # Check if the text contains an ingredient
    def check_for_ingredient(self):
        # works only if the ingredient is a single word
        for token in self.doc:
            if token.text in ingredients_list:
                return token.text
        # works if the ingredient is a multi-word phrase
        for token in self.doc:
            if token.head.text in ingredients_list:
                ingredient = token.text + " " + token.head.text
                if ingredient in ingredients_list:
                    return ingredient
        return None

    # Check if the text is positive or negative
    def check_positivity(self):
        self.positivity = True
        for token in self.doc:
            if "Neg" in token.morph.get("Polarity"):
                self.positivity = False
        return self.positivity


if __name__ == "__main__":
    analysis = Analysis("There is bubotuber pus in the polyjuice potion.")
    print(analysis.text)
    # pprint(analysis.doc.to_json())
    pprint(analysis.get_dependecies())
    print(f"Found ingredient: {analysis.check_for_ingredient()}")
    print(f"Positivity: {analysis.positivity}")
    # displacy.serve(analysis.doc, style="dep")
