import potion


class Frame:
    def __init__(self, target_potion: potion.Potion, current_ingredients=None):
        if current_ingredients is None:
            current_ingredients = []
        self.target_potion = target_potion
        self.current_ingredients = set(current_ingredients)
        self.wrong_ingredients = 0
        self.is_completed = False

    def __str__(self):
        return f"{self.target_potion} \n Current ingredients: {', '.join(self.current_ingredients)} \n Wrong ingredients: {self.wrong_ingredients}"

    def get_target_potion(self):
        return self.target_potion

    def get_current_ingredients(self):
        return self.current_ingredients

    def get_wrong_ingredients(self):
        return self.wrong_ingredients

    def check_if_complete(self):
        if self.current_ingredients == set(self.target_potion.get_ingredients()):
            self.is_completed = True
        return self.is_completed

    def add_ingredient(self, ingredient):
        if ingredient in self.target_potion.get_ingredients():
            self.current_ingredients.add(ingredient)
        else:
            self.wrong_ingredients += 1


if __name__ == "__main__":
    frame = Frame(potion.Potion("Invisibility", ["Eye of Newt", "Dragon's Blood"]))
    print(frame)
    # print(frame.get_target_potion())
    # print(frame.is_completed())
    frame.add_ingredient("Eye of Newt")
    print(frame)
    frame.add_ingredient("Dragon's Blood")
    print(frame)
    frame.add_ingredient("Wrong ingredient")
    print(frame)
    print(frame.check_if_complete())
