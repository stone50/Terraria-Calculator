import math
import dataHandler

allRecipes = dataHandler.getAllRecipes()

def updateAllRecipes():
    dataHandler.updateRecipeData()
    allRecipes = dataHandler.getAllRecipes()

def findIngredients(itemName, itemCount = 1):
    if not itemName in allRecipes:
        return None
    return _findIngredientsRecurive(itemName, itemCount)

def _findIngredientsRecurive(itemName, itemCount = 1):
    itemMultiplier = math.ceil(itemCount / allRecipes[itemName].amount)

    outRecipe = dataHandler.Recipe(
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