import product_manager as pm

def test_create_product():
    product = {"id": 1, "name": "Laptop", "price": 1200}
    result = pm.create_product(product)
    assert result["name"] == "Laptop"

def test_read_products():
    products = pm.read_products()
    assert isinstance(products, list)

def test_update_product():
    updated = pm.update_product(1, {"price": 1000})
    assert updated["price"] == 1000

def test_delete_product():
    result = pm.delete_product(1)
    assert result is True