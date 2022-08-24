import requests
import re
import dataHandler

def pullResultName(tableRow):
    return re.search(r"title=\"(.+?)\"", tableRow).group(1)

def pullResultAmount(tableRow):
    amount = re.search(r"<span class=\"note-text\">(.+?)</span>", tableRow)
    if amount:
        return amount.group(1)[1:-1]
    return 1

def pullResult(tableRow):
    return dataHandler.RecipeResult(
        pullResultName(tableRow),
        pullResultAmount(tableRow)
    )

def pullIngredientName(listItem):
    return re.search(r"title=\"(.+?)\"", listItem).group(1)

def pullIngredientAmount(listItem):
    foundAmount = re.search(r"<span class=\"note-text\">(.+?)</span>", listItem)
    if foundAmount:
        return foundAmount.group(1)[1:-1]
    return 1

def pullIngredients(tableRow):
    ingredients = []
    for listItem in re.findall(r"<li>.+?</li>", tableRow):
        ingredients.append(dataHandler.RecipeIngredient(
            pullIngredientName(listItem),
            pullIngredientAmount(listItem)
        ))
    return ingredients

def pullRecipe(tableRow):
    return dataHandler.Recipe(
        pullResult(tableRow),
        pullIngredients(tableRow)
    )
    
def pullRecipes(tableBody):
    recipes = []
    for tableRow in re.findall(r"<tr data-rowid=\".+?\">.+?</tr>", tableBody):
        recipes.append(pullRecipe(tableRow))
    return recipes

def pullTableBody(html):
    return re.search(r"<table class=\"crafts\">.+?<table.*?>(<tbody>.+?</tbody>)", html).group(1)

def pullCraftingRecipes(url):
    return pullRecipes(pullTableBody(requests.get(url).text))  

def pullStations(html):
    return re.findall(r"data-ajax-source-page=\"Recipes/(.+?)\"", html)

def pullAllCraftingRecipes():
    allRecipes = []
    for station in pullStations(requests.get("https://terraria.fandom.com/wiki/Recipes").text):
        allRecipes += pullCraftingRecipes(f'https://terraria.fandom.com/wiki/Recipes/{station.replace(" ", "_").replace("&#39;", "%27")}')
    return allRecipes