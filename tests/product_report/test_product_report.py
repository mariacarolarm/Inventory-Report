from inventory_report.product import Product


def test_product_report() -> None:
    fake_product = Product(
        id="12345",
        product_name="Example Product",
        company_name="Example Company",
        manufacturing_date="2023-01-01",
        expiration_date="2025-01-01",
        serial_number="SN123456789",
        storage_instructions="Store in a cool, dry place."
    )

    expected_str = (
        f"The product {fake_product.id} - {fake_product.product_name} "
        f"with serial number {fake_product.serial_number} "
        f"manufactured on {fake_product.manufacturing_date} "
        f"by the company {fake_product.company_name} "
        f"valid until {fake_product.expiration_date} "
        "must be stored according to the following instructions: "
        f"{fake_product.storage_instructions}."
    )

    assert str(fake_product) == expected_str
