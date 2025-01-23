**Recipe Finder with Rich Display**

Project Description:

This Python script allows users to fetch and display recipe details based on a main ingredient using the Spoonacular API. The recipes are presented in a beautifully formatted table using the rich library for enhanced console output.

<hr/>

Features:

1. Fetches recipes based on a main ingredient entered by the user.
2. Allows users to specify the number of recipes to display.
3. Displays detailed recipe information including:
* Recipe title
* Cuisines
* Dish types
* Preparation time
* Serving size
* Gluten-free status
* Health score
4. Stylish, readable output using rich.table with custom styling and formatting.

<hr/>

Prerequisites:

* Python 3.6 or later
* An active API key from Spoonacular API

<hr/>

Installation:

1. Clone this repository or copy the script.
2. Install the required libraries: pip install requests rich

<hr/>

Usage:

1. Update the API_KEY variable in the script with your Spoonacular API key.
2. Run the script: python recipe_finder.py
3. Follow the prompts:
* Enter the main ingredient (e.g., Chicken, Pasta).
* Specify the number of recipes to fetch.

<hr/>

Example Output:

Enter the main Ingredient of the recipe (Ex: Chicken, Pasta etc.): chicken

Enter the number of recipes you would like to view: 3

<hr/>

Notes:

* Ensure the API key is valid; otherwise, the script will not retrieve data.
* The script uses rich to enhance the terminal display; ensure your terminal supports rich formatting.
