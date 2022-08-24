import pickle
import scraper

class RecipeResult:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __str__(self):
        return f'Name: {self.name} Amount: {self.amount}'
    
    def __repr__(self):
        return f'Name: {self.name} Amount: {self.amount}'

class RecipeIngredient:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def __str__(self):
        return f'Name: {self.name} Amount: {self.amount}'
    
    def __repr__(self):
        return f'Name: {self.name} Amount: {self.amount}'

class Recipe:
    def __init__(self, result, ingredients):
        self.result = result
        self.ingredients = ingredients

    def __str__(self):
        return f'Result: {self.result} Ingredients: {self.ingredients}'
    
    def __repr__(self):
        return f'Result: {self.result} Ingredients: {self.ingredients}'

def updateRecipeData():
    with open('recipes.bin', 'wb') as recipeFile:
        pickle.dump(scraper.pullAllCraftingRecipes(), recipeFile)

def getAllRecipes():
    with open('config.dictionary', 'rb') as recipeFile:
        return pickle.load(recipeFile)