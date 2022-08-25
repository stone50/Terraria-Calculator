from requests import get as requestGet
from re import search as reSearch, findall as reFindall
from html import unescape as htmlUnescape
from .Recipe import Recipe

def pullResultName(tableRow):
    return reSearch(r"title=\"(.+?)\"", tableRow).group(1)

def pullResultAmount(tableRow):
    amount = reSearch(r"<td class=\"result\".*?><span class=\"note-text\">(.+?)</span></td>", tableRow)
    if amount:
        return int(amount.group(1)[1:-1])
    return 1

def pullIngredientName(listItem):
    return reSearch(r"title=\"(.+?)\"", listItem).group(1)

def pullIngredientAmount(listItem):
    foundAmount = reSearch(r"<span class=\"note-text\">(.+?)</span>", listItem)
    if foundAmount:
        return int(foundAmount.group(1)[1:-1])
    return 1

def pullIngredients(tableRow):
    ingredients = {}
    for listItem in reFindall(r"<li>.+?</li>", tableRow):
        ingredients[pullIngredientName(listItem)] = pullIngredientAmount(listItem)
    return ingredients

def pullRecipe(tableRow):
    return Recipe(
        pullResultName(tableRow),
        pullResultAmount(tableRow),
        pullIngredients(tableRow),
        'Unknown'
    )
    
def pullRecipes(tableBody):
    recipes = {}
    for tableRow in reFindall(r"<tr data-rowid=\".+?\">.+?</tr>", tableBody):
        recipe = pullRecipe(tableRow)
        if not recipe.result in recipes:
            recipes[recipe.result] = recipe
    return recipes

def pullTableBody(html):
    return reSearch(r"<table class=\"crafts\">.+?<table.*?>(<tbody>.+?</tbody>)", html).group(1)

def pullCraftingRecipes(url):
    return pullRecipes(htmlUnescape(pullTableBody(requestGet(url).text)))  

def pullStations(html):
    return reFindall(r"data-ajax-source-page=\"Recipes/(.+?)\"", html)

def pullAllCraftingRecipes():
    allRecipes = {}
    for station in pullStations(htmlUnescape(requestGet("https://terraria.fandom.com/wiki/Recipes").text)):
        stationRecipes = pullCraftingRecipes(f'https://terraria.fandom.com/wiki/Recipes/{station.replace(" ", "_")}')
        for recipe in stationRecipes:
            stationRecipes[recipe].station = station
            allRecipes[recipe] = stationRecipes[recipe]
    return allRecipes