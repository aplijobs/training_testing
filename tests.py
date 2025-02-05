import pytest
from base_class import Product, ShoppingCart


def test_product_initialization():
    product = Product("Apple", 1.2)
    assert product.name == "Apple"
    assert product.price == 1.2


def test_shopping_cart_initialization():
    cart = ShoppingCart("John Doe")
    assert cart.client_name == "John Doe"
    assert cart.items == []
    assert cart.total == 0.0


def test_add_product_to_cart():
    cart = ShoppingCart("John Doe")
    product = Product("Apple", 1.2)
    cart.add_product(product, 3)
    assert len(cart.items) == 1
    assert cart.items[0]['product'] == product
    assert cart.items[0]['quantity'] == 3
    assert cart.total == 3 * 1.2


def test_remove_product_from_cart():
    cart = ShoppingCart("John Doe")
    product = Product("Apple", 1.2)
    cart.add_product(product, 3)
    cart.remove_product("Apple", 2)
    assert len(cart.items) == 1
    assert cart.items[0]['quantity'] == 1
    assert cart.total == 1 * 1.2


def test_clear_cart():
    cart = ShoppingCart("John Doe")
    product = Product("Apple", 1.2)
    cart.add_product(product, 3)
    cart.clear_cart()
    assert cart.items == []
    assert cart.total == 0.0


def test_checkout():
    cart = ShoppingCart("John Doe")
    product1 = Product("Apple", 1.2)
    product2 = Product("Banana", 0.5)
    cart.add_product(product1, 3)
    cart.add_product(product2, 5)
    receipt = cart.checkout()
    assert "Receipt for John Doe:" in receipt
    assert "- Apple (x3): $3.60" in receipt
    assert "- Banana (x5): $2.50" in receipt
    assert "Total: $6.10" in receipt
    assert cart.items == []
    assert cart.total == 0.0


def test_checkout_empty_cart():
    cart = ShoppingCart("John Doe")
    with pytest.raises(ValueError, match="Cannot checkout an empty cart"):
        cart.checkout()
