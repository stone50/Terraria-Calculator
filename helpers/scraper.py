import requests
import re
import html
import dataHandler

def pullResultName(tableRow):
    return re.search(r"title=\"(.+?)\"", tableRow).group(1)

def pullResultAmount(tableRow):
    amount = re.search(r"<td class=\"result\".*?><span class=\"note-text\">(.+?)</span></td>", tableRow)
    if amount:
        return int(amount.group(1)[1:-1])
    return 1

def pullIngredientName(listItem):
    return re.search(r"title=\"(.+?)\"", listItem).group(1)

def pullIngredientAmount(listItem):
    foundAmount = re.search(r"<span class=\"note-text\">(.+?)</span>", listItem)
    if foundAmount:
        return int(foundAmount.group(1)[1:-1])
    return 1

def pullIngredients(tableRow):
    ingredients = {}
    for listItem in re.findall(r"<li>.+?</li>", tableRow):
        ingredients[pullIngredientName(listItem)] = pullIngredientAmount(listItem)
    return ingredients

def pullRecipe(tableRow):
    return dataHandler.Recipe(
        pullResultName(tableRow),
        pullResultAmount(tableRow),
        pullIngredients(tableRow),
        'Unknown'
    )
    
def pullRecipes(tableBody):
    recipes = {}
    for tableRow in re.findall(r"<tr data-rowid=\".+?\">.+?</tr>", tableBody):
        recipe = pullRecipe(tableRow)
        if not recipe.result in recipes:
            recipes[recipe.result] = recipe
    return recipes

def pullTableBody(html):
    return re.search(r"<table class=\"crafts\">.+?<table.*?>(<tbody>.+?</tbody>)", html).group(1)

def pullCraftingRecipes(url):
    return pullRecipes(html.unescape(pullTableBody(requests.get(url).text)))  

def pullStations(html):
    return re.findall(r"data-ajax-source-page=\"Recipes/(.+?)\"", html)

def pullAllCraftingRecipes():
    allRecipes = {}
    for station in pullStations(html.unescape(requests.get("https://terraria.fandom.com/wiki/Recipes").text)):
        stationRecipes = pullCraftingRecipes(f'https://terraria.fandom.com/wiki/Recipes/{station.replace(" ", "_")}')
        for recipe in stationRecipes:
            stationRecipes[recipe].station = station
            allRecipes[recipe] = stationRecipes[recipe]
    return allRecipes