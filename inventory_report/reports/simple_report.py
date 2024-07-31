from typing import List
from datetime import datetime
from inventory_report.inventory import Inventory


class SimpleReport:
    def __init__(self):
        self.inventories: List[Inventory] = []

    def add_inventory(self, inventory: Inventory) -> None:
        self.inventories.append(inventory)

    def get_oldest_date(self) -> str:
        return min(
            product.manufacturing_date for inventory in
            self.inventories for product in inventory.data
        )

    def get_expiration_date(self) -> str:
        return min(
            product.expiration_date for inventory in
            self.inventories for product in inventory.data
            if datetime.strptime(product.expiration_date,
                                 "%Y-%m-%d") >= datetime.now()
        )

    def get_largest_inventory(self) -> str:
        all_products = []
        for inventory in self.inventories:
            all_products.extend(inventory.data)

        company_inventory_count = {}
        for product in all_products:
            company_inventory_count[product.company_name] = (
                company_inventory_count.get(product.company_name, 0) + 1
            )
        largest_inventory = max(company_inventory_count,
                                key=company_inventory_count.get)

        return largest_inventory

    def generate(self) -> str:
        oldest = self.get_oldest_date()
        closest = self.get_expiration_date()
        largest_inventory = self.get_largest_inventory()

        return (
            f"Oldest manufacturing date: {oldest}\n"
            f"Closest expiration date: {closest}\n"
            f"Company with the largest inventory: {largest_inventory}"
        )
