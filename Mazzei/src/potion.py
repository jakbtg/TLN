class Potion:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def __str__(self):
        return f'{self.name}\n\tIngredients: {", ".join(self.ingredients)}'

    def get_name(self):
        return self.name

    def get_ingredients(self):
        return self.ingredients


if __name__ == "__main__":
    potion = Potion(
        "Healing Potion",
        ["Wormwood", "Bubotuber pus", "Dittany", "Dragon liver", "Unicorn tailhair"],
    )
    print(potion)
    print(potion.get_name())
    print(potion.get_ingredients())
