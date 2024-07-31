from inventory_report.product import Product


def test_create_product() -> None:
    fake_product = Product(
            id="12345",
            product_name="Example Product",
            company_name="Example Company",
            manufacturing_date="2023-01-01",
            expiration_date="2025-01-01",
            serial_number="SN123456789",
            storage_instructions="Store in a cool, dry place."
        )

    assert fake_product.id == "12345"
    assert fake_product.product_name == "Example Product"
    assert fake_product.company_name == "Example Company"
    assert fake_product.manufacturing_date == "2023-01-01"
    assert fake_product.expiration_date == "2025-01-01"
    assert fake_product.serial_number == "SN123456789"
    assert fake_product.storage_instructions == "Store in a cool, dry place."
