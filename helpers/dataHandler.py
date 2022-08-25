from os.path import dirname
from pickle import dump as pickleDump, load as pickleLoad, HIGHEST_PROTOCOL
from .scraper import pullAllCraftingRecipes as scrapeAllRecipes

def updateRecipeData():
    with open(dirname(__file__) + '\\recipes.bin', 'wb') as recipeFile:
        pickleDump(scrapeAllRecipes(), recipeFile, protocol=HIGHEST_PROTOCOL)

def getAllRecipes():
    with open(dirname(__file__) + '\\recipes.bin', 'rb') as recipeFile:
        return pickleLoad(recipeFile)