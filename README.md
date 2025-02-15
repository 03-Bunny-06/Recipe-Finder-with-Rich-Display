# Recipe Finder with Rich Display

## Project Description

This Python script allows users to fetch and display recipe details based on a main ingredient using the **Spoonacular API**. The recipes are presented in a beautifully formatted table using the **rich** library for enhanced console output.

## Features

- Fetches recipes based on a main ingredient entered by the user.
- Allows users to specify the number of recipes to display.
- Displays detailed recipe information including:
  - **Recipe title**
  - **Cuisines**
  - **Dish types**
  - **Preparation time**
  - **Serving size**
  - **Gluten-free status**
  - **Health score**
- Stylish, readable output using `rich.table` with custom styling and formatting.

## Prerequisites

- **Python 3.6 or later**
- An active API key from **Spoonacular API**

## Installation

1. Clone this repository or copy the script.
2. Install the required libraries:
   
   ```bash
   pip install requests rich
   ```

## Usage

1. Update the `API_KEY` variable in the script with your **Spoonacular API key**.
2. Run the script:
   
   ```bash
   python recipe_finder.py
   ```

3. Follow the prompts:
   - Enter the main ingredient (e.g., **Chicken, Pasta**).
   - Specify the number of recipes to fetch.

## Example Output

```plaintext
Enter the main Ingredient of the recipe (Ex: Chicken, Pasta etc.): chicken

Enter the number of recipes you would like to view: 15



Enter the main Ingredient of the recipe (Ex: Chicken, Pasta etc.): pasta

Enter the number of recipes you would like to view: 10

![image](https://github.com/user-attachments/assets/01abc74f-ca3c-4043-99d3-0a40e46ba2fa)
```

![image](https://github.com/user-attachments/assets/28960b62-e760-434f-be49-d26c355e6fb0)

```plaintext
Enter the main Ingredient of the recipe (Ex: Chicken, Pasta etc.): pasta

Enter the number of recipes you would like to view: 10
```

![image](https://github.com/user-attachments/assets/01abc74f-ca3c-4043-99d3-0a40e46ba2fa)

## Notes

- Ensure the **API key** is valid; otherwise, the script will not retrieve data.
- The script uses **rich** to enhance the terminal display; ensure your terminal supports rich formatting.
