# ------------------------------------------------------------------------------

# Sheet 3 Exercise 9 - Resubmission

# Niklas Markert - 1611460 / bt70985

# ------------------------------------------------------------------------------

inventory_bakery = {'Flour': 23485, 'Salt': 329, 'Yeast': 834}
recipe_bread = {'Flour': 500, 'Water': 300, 'Salt': 9, 'Yeast': 30}


# ------------
# a)
# ------------

def possible_amount_bread(inventory, recipe):
    """
    Calculates the amount maximum amount ob bread you can possible bake with the given inventory.

    :param inventory: The inventory you have to bake bread
    :param recipe: The recipe for one loaf bread
    :return: The possible amount of loafs bread you can bake
    """

    # Short from for iterating over all ingredients of the recipe except 'Water'
    return min([inventory[ingredient]//recipe[ingredient] for ingredient in recipe.keys() if ingredient != 'Water'])


amount_bread = possible_amount_bread(inventory_bakery, recipe_bread)
print('With your inventory you can bake', amount_bread, 'breads.')


def bake_breads(amount, inventory, recipe):
    """
    Updates the inventory based on how many loafs breads you baked.

    :param amount: The amount of loafs
    :param inventory: The inventory you had
    :param recipe: The recipe for one loaf bread
    :return: None
    """
    for ingredient in recipe.keys():    # Iterating over all ingredients of the recipe
        if ingredient == 'Water':       # Skipping the ingredient 'Water', because the bakery has an infinite amount of
            continue                    # water
        inventory[ingredient] -= amount * recipe[ingredient]


bake_breads(amount_bread, inventory_bakery, recipe_bread)
print('Inventory after baking the maximum amount of breads:', inventory_bakery)


# ------------
# b)
# ------------


def get_shopping_list(amount_loafs, inventory, recipe):
    """
    Calculates the shopping list, based on your inventory and the amount of loafs you are planning to bake.

    :param amount_loafs: The amount of loafs you want to bake
    :param inventory: Your current inventory
    :param recipe: The recipe for one loaf bread
    :return: The calculated shopping list
    """
    package_sizes = {'Flour': 1000, 'Salt': 250, 'Yeast': 100}
    shopping_list = {}

    for ingredient in recipe.keys():    # Iterating over all ingredients of the recipe
        if ingredient == 'Water':       # Skipping the ingredient 'Water', because the bakery has an infinite amount of
            continue                    # water
        needed_amount = max(recipe[ingredient] * amount_loafs - inventory[ingredient], 0)
        shopping_list[ingredient] = needed_amount // package_sizes[ingredient] \
            + 1 if needed_amount % package_sizes[ingredient] > 0 else 0

    return shopping_list


print('Shopping list:', get_shopping_list(150, inventory_bakery, recipe_bread))
