from helpers.calculator import allRecipes, updateAllRecipes, findIngredients

'''
Useful functions and variables

allRecipes = a dictionary of all recipes

updateAllRecipes() = updates all recipes

note:   This scrapes the Terraria wiki.
        This could fail if the wiki is updated.
        This is relatively slow.
        Recommended to only use this if the crafting recipes change

findIngredients(itemName, itemCount) = returns a nested recipe

note:   Recipes returned will be of the format:
        {
            'result': string
            'amount': int
            'ingredients': {
                'ingredient': Recipe or int
            }
            'station': string
        }
'''

# Example
print(findIngredients("Night's Edge"))