from typing import Dict, Type, List
from abc import ABC, abstractmethod
from inventory_report.product import Product
import json
import csv


class Importer(ABC):
    def __init__(self, path: str):
        self.file_path = path

    @abstractmethod
    def import_data(self) -> List[Product]:
        pass


class JsonImporter(Importer):
    def import_data(self) -> List[Product]:
        with open(self.file_path) as file:
            products = json.load(file)
            return [Product(**product) for product in products]


class CsvImporter(Importer):
    def import_data(self) -> List[Product]:
        with open(self.file_path) as file:
            products = list(csv.DictReader(file))
            return [Product(**product) for product in products]


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
