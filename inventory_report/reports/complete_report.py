from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def generate(self) -> str:
        basic_report = super().generate()

        all_products = []
        for inventory in self.inventories:
            all_products.extend(inventory.data)

        company_inventory_count = Counter(
            product.company_name for product in all_products
        )

        company_stock_report = "\n".join(
            f"- {company}: {count}" for company,
            count in company_inventory_count.items()
        )

        return (
            f"{basic_report}\n"
            f"Stocked products by company:\n"
            f"{company_stock_report}"
        )
