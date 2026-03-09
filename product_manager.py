import json
import os

FILE_PATH = "products.json"

def load_data():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as f:
        return json.load(f)

def save_data(data):
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)

def create_product(product):
    data = load_data()
    data.append(product)
    save_data(data)
    return product

def read_products():
    return load_data()

def update_product(product_id, new_data):
    data = load_data()

    for product in data:
        if product.get("id") == product_id:
            product.update(new_data)
            save_data(data)
            return product

    return None

def delete_product(product_id):
    data = load_data()

    new_data = [p for p in data if p.get("id") != product_id]

    if len(new_data) == len(data):
        return False

    save_data(new_data)
    return True