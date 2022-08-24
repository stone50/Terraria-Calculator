from types import NoneType
import dataHandler

class IngredientsSearchResult:
    def __init__(self, )

def findIngredients(itemName, recipeList):
    foundRecipe = None
    for recipe in recipeList:
        if recipe.name == itemName:
            foundRecipe = recipe
            break
    if not foundRecipe:
        return []
    ingredients = []
