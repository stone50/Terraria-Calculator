import pickle
import scraper

class Recipe:
    def __init__(self, result, amount, ingredients, station):
        self.result = result
        self.amount = amount
        self.ingredients = ingredients
        self.station = station

    def __str__(self):
        return f"{{\n\t'Result': {self.result}\n\t'Amount': {self.amount}\n\t'Ingredients': {self.ingredients}\n\t'Station': {self.station}\n}}\n"
    
    def __repr__(self):
        return f"{{\n\t'Result': {self.result}\n\t'Amount': {self.amount}\n\t'Ingredients': {self.ingredients}\n\t'Station': {self.station}\n}}\n"

def updateRecipeData():
    with open('recipes.bin', 'wb') as recipeFile:
        pickle.dump(scraper.pullAllCraftingRecipes(), recipeFile)

def getAllRecipes():
    with open('recipes.bin', 'rb') as recipeFile:
        return pickle.load(recipeFile)