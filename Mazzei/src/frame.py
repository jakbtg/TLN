from potions_list import *


class Frame:
    def __init__(self, target_potion, current_ingredients=None):
        if current_ingredients is None:
            current_ingredients = []
        self.target_potion = target_potion
        self.current_ingredients = set(current_ingredients)
        self.is_completed = False

    def __str__(self):
        return f"{self.target_potion}\n\tCurrent ingredients: {', '.join(self.current_ingredients)}"

    def get_target_potion(self):
        return self.target_potion

    def get_target_ingredients(self):
        ingredients = self.get_target_potion().get_ingredients()
        result = []
        for ingredient in ingredients:
            result.append(ingredient.lower())
        return result

    def get_current_ingredients(self):
        return self.current_ingredients

    # Check if the current ingredients are the same as the target potion ingredients
    def check_if_complete(self):
        if self.current_ingredients == set(self.get_target_ingredients()):
            self.is_completed = True
        return self.is_completed

    # Add a list of ingredients to the current ingredients
    def add_ingredient(self, ingredients):
        ingredients = set(ingredients)
        for ingredient in ingredients:
            self.check_casefold_and_add(ingredient)

    # Check if the ingredient is in the target potion ingredients ignoring the case
    # - If the ingredient is in the target potion, add it to the current ingredients
    # - If the ingredient is not in the target potion, print the wrong ingredient
    def check_casefold_and_add(self, ingredient):
        found = False
        for target_ingredient in self.target_potion.get_ingredients():
            if ingredient.casefold() == target_ingredient.casefold():
                self.current_ingredients.add(ingredient.lower())
                found = True
        if not found:
            print(f"Wrong ingredient: {ingredient}")


if __name__ == "__main__":
    frame = Frame(polyjuice_potion)
    print(frame)
    frame.add_ingredient(["Lacewing flies", "leeches"])
    print(frame)
    # Trying to add an existing ingredient which is not in the target potion
    frame.add_ingredient(["Dragon liver"])
    print(frame)
    # Trying to add a fake ingredient
    frame.add_ingredient(["Wrong ingredient"])
    print(frame)
    frame.add_ingredient(
        [
            "powdered bicorn horn",
            "knotgrass",
            "Fluxweed",
            "Shredded Boomslang skin",
            "hair",
        ]
    )
    print(frame)
    print(f"Is completed: {frame.check_if_complete()}")
