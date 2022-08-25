from math import ceil
from .dataHandler import getAllRecipes, updateRecipeData
from .Recipe import Recipe

allRecipes = getAllRecipes()

def updateAllRecipes():
    updateRecipeData()
    allRecipes = getAllRecipes()

def findIngredients(itemName, itemCount = 1):
    if not itemName in allRecipes:
        return None
    return _findIngredientsRecurive(itemName, itemCount)

def _findIngredientsRecurive(itemName, itemCount = 1):
    itemMultiplier = ceil(itemCount / allRecipes[itemName].amount)

    outRecipe = Recipe(
        itemName,
        allRecipes[itemName].amount * itemMultiplier,
        {},
        allRecipes[itemName].station
    )

    for ingredient in allRecipes[itemName].ingredients:
        ingredientAmount = allRecipes[itemName].ingredients[ingredient] * itemMultiplier
        if ingredient in allRecipes:
            if itemName in allRecipes[ingredient].ingredients:
                outRecipe.ingredients[ingredient] = ingredientAmount
            else:
                iIngredients = _findIngredientsRecurive(ingredient, ingredientAmount)
                outRecipe.ingredients[ingredient] = iIngredients
        else:
            outRecipe.ingredients[ingredient] = ingredientAmount
    
    return outRecipe