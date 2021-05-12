# ------------------------------------------------------------------------------

# Sheet 3 Exercise 9

# Niklas Markert - 1611460 / bt70985
# Lukas Thiersch - 1607110 / bt708626

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
    amounts = []

    for ingredient in recipe.keys():
        amounts.append(inventory[ingredient] // recipe[ingredient])

    return min(amounts)


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
    for ingredient in recipe.keys():
        inventory[ingredient] -= amount * recipe[ingredient]

    # In the exercise it says: "using (one of) the above operator(s)".
    # But we came to the conclusion that the use of neither // or % are
    # useful here. We thought about using % to calculate the rest of one
    # ingredient that is left after baking the bread (that is essentially
    # what we are doing in this method) but this fails when we can bake
    # more bread with one ingredient than with the other. Assume for
    # example we need 100g of flour and salt for a bread and we have 500g
    # of flour and 1500g of salt: We can just bake 5 Breads and thus we
    # have 0g flour and 1000g salt left. But if we use % for calculating
    # the remaining ingredients, we will have 0g of both left because 5
    # breads * 100g = 500g and 500g % 500g = 0g but also 1500g % 500g = 0g.


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
