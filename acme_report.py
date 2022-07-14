import random

from acme import Product


ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    result = []
    for x in range(num_products):
        rand_name = random.choice(ADJECTIVES) + ' ' + random.choice(NOUNS)
        rand_price = random.randint(5, 100)
        rand_weight = random.randint(5, 100)
        rand_flam = random.uniform(0.0, 2.5)
        product = Product(rand_name, rand_price, rand_weight, rand_flam)
        result.append(product)
    return result


def inventory_report(product_list):
    return ('unique names', 'avg price', 'avg weight', 'avg flam')