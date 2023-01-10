import spacy
from potions_list import ingredients_list


class Analysis:
    def __init__(self, text):
        self.text = text.lower()
        self.nlp = spacy.load("en_core_web_md")
        self.doc = self.nlp(self.text)

    # Get the dependencies of the text in the form:
    # {token: (dependency, part of speech, head)}
    # --> used to understand how to work with spacy
    def get_dependecies(self):
        dict = {}
        for token in self.doc:
            dict[token.text] = token.dep_, token.pos_, token.head.text
        return dict

    # Check if the text contains an ingredient
    def check_for_ingredient(self):
        found = []
        ingredients_words_list = [ingredient.split() for ingredient in ingredients_list]
        for token in self.doc:
            for ingredient_words in ingredients_words_list:
                if token.text == ingredient_words[0]:
                    if len(ingredient_words) == 1:
                        found.append(token.text)
                    # if it is the last token of the text and the ingredient is made of more than one word, it must be wrong
                    elif token.i == len(self.doc) - 1 and len(ingredient_words) > 1:
                        found.append(None)
                    else:
                        found.append(
                            self.scan_neighbour_tokens(token, ingredient_words)
                        )
        found = [x for x in found if x is not None]
        return found

    # Scan the neighbour tokens to find the whole ingredient
    # Needed because some ingredients are made of more than one word
    def scan_neighbour_tokens(self, token, ingredient_words):
        for i in range(1, len(ingredient_words)):
            # if it is the last token of the text and the ingredient is made of more than one word, it must be wrong
            if token.i + i == len(self.doc) and len(ingredient_words) > 1:
                return None
            # if the neighbour token is not the same as the ingredient word, it must be wrong
            if token.nbor(i).text != ingredient_words[i]:
                return None
        return " ".join(ingredient_words)

    # Check if the text is positive or negative
    def check_positivity(self):
        self.positivity = True
        for token in self.doc:
            if "Neg" in token.morph.get("Polarity") or token.text == "no":
                self.positivity = False
        return self.positivity

    # Count number of ingredients in the text --> used to check if the question is valid
    def number_of_ingredients(self):
        return len(self.check_for_ingredient())


if __name__ == "__main__":
    analysis = Analysis("You don't need any lacewing flies")
    print(analysis.text)
    print("\n")
    dependencies = analysis.get_dependecies()
    for key, value in dependencies.items():
        print(f"{key}: {value}")
    print("\n")
    print(f"Found ingredient: {analysis.check_for_ingredient()}")
    print(f"Positivity: {analysis.check_positivity()}")
    print(f"Number of ingredients: {analysis.number_of_ingredients()}")
