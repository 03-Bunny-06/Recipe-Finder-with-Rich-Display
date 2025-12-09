# Code
import requests

from rich.console import Console
from rich.table import Table
from rich.box import SQUARE_DOUBLE_HEAD

console = Console()

BASE_URL = "https://api.spoonacular.com/recipes/complexSearch"
API_KEY = apikey
RECIPE_INFO = "true"

def recipe(main_item, number):
    url = f'{BASE_URL}?query={main_item}&number={number}&addRecipeInformation={RECIPE_INFO}&apiKey={API_KEY}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to retrive the Data.")
        return None


main_item = input('Enter the main Ingredient of the recipe (Ex: Chicken, Pasta etc.): ').lower()
number = int(input('Enter the number of recipes you would like to view: '))

res = recipe(main_item, number)
if res:
    rec = res['results']
    table = Table(title=f"The {main_item.upper()} Recipes",style='cyan', border_style='green', box=SQUARE_DOUBLE_HEAD)
    table.add_column('Title', min_width=25, justify="default")
    table.add_column('Cuisines', max_width=20, justify="center")
    table.add_column('Dish Types', min_width=20, justify="center")
    table.add_column('Ready in Minutes', max_width=20, justify="center")
    table.add_column("Servings Size", max_width=15, justify="center")
    table.add_column("Gluten Free", max_width=15, justify="center")
    table.add_column("Health Score", max_width=15, justify="center")
    for i in range(len(rec)):
        new_recipe = res['results'][i]
        # Cuisines
        cuisi = new_recipe['cuisines']
        cus = ''
        if (len(cuisi) == 0):
            cus = '-'
        else:
            for i in cuisi:
                cus += i + ' '
        # Dish Types
        dish = new_recipe['dishTypes']
        dis = ''
        if (len(dish) == 0):
            cus = 'Not Secific'
        else:
            for j in dish:
                dis += j + ','
        dis = dis.upper()

        table.add_row(new_recipe['title'], cus, dis[:-1], f'{new_recipe['readyInMinutes']} min', str(new_recipe['servings']), str(new_recipe['glutenFree']), f'{new_recipe['healthScore']}/100')

    console.print(table)
