class Potion:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def __str__(self):
        return f'{self.name} ({", ".join(self.ingredients)})'
