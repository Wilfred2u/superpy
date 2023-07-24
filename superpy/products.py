from pathlib import Path
import json


def show_all_products():
    """Return a list of all available products."""
    path = Path('products.json')
    contents = path.read_text()
    products = json.loads(contents)

    all_products = [row['product_name'] for row in products]
    return all_products
