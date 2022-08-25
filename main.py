import helpers.calculator as calculator

'''
Useful functions and variables

calculator.allRecipes = a dictionary of all recipes

calculator.updateAllRecipes() = updates all recipes

note:   This scrapes the Terraria wiki.
        This could fail if the wiki is updated.
        This is relatively slow.
        Recommended to only use this if the crafting recipes change

calculator.findIngredients(itemName, itemCount) = returns a nested recipe

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
print(calculator.findIngredients("Night's Edge"))