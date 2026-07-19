from abc import ABCMeta
from registry.registry import ProductRegistry


class ProductMeta(ABCMeta):
    def __new__(mcls, name, bases, namespace):
        cls = super().__new__(mcls, name, bases, namespace)

        # Don't register the abstract base class itself.
        if not namespace.get("__abstractmethods__") and name != "BaseProduct":
            ProductRegistry.register(cls)

        return cls
