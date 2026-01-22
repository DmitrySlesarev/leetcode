from decimal import Decimal

import pytest


class PriceManager:
    def __init__(self,
                 x_price_source: PriceSource,
                 y_price_source: PriceSource,
                 ) -> None:
        ...

    def get_price(self, product: Product) -> Decimal | None:
        if product.type == "x":
            return self.x_price_source.get(product)
        elif product.type == "y":
            return self.y_price_source.get(product)
        else:
            return None

class TestPriceManager:
    def test_get_price_if_prodect_type_eq_x(self) -> None:
        product = Product(type="x")
        price_manager = PriceManager(
            x_price_source=StubXPriceSource(return_result=Decimal("150.00")),
            y_price_source=StubYPriceSource(return_result=Decimal("220.00"))
        )

        got = price_manager.get_price(product)

        assert got == Decimal("150.00")

    def test_get_price_if_product_type_eq_y(self) -> None:
        product = Product(type="y")
        price_manager = PriceManager(
            x_price_source = StubXPriceSource(return_result=Decimal("150.00")),
            y_price_source = StubYPriceSource(return_result=Decimal("220.00")),
        )

        got = price_manager.get_price(product)

        assert got == Decimal("220.00")

    def test_get_price_if_product_type_unknown(self) -> None:
        product = Product(type="unknown_product_type")
        price_manager = PriceManager(
            x_price_source=StubXPriceSource(return_result=Decimal("150.00")),
            y_price_source=StubYPriceSource(return_result=Decimal("200.00")),
        )

        got = price_manager.get_price(product)

        assert got == None

# ------------------------------------

def price_manager() -> PriceManager:
    return PriceManager(
        x_price_source=StubXPriceSource(return_result=Decimal("150.00")),
        y_price_source=StubYPriceSource(return_result=Decimal("200.00")),
    )

class TestPriceManager:
    def test_get_price_if_product_type_eq_x(self) -> None:
        product = Product(type="x")

        # AAA = "Arrange Act Assert"
        price_manager = price_manager()

        got = price_manager.get_price(product)

        assert got == Decimal("150.00")

# ------------------------------------

@pytest.fixture()
def price_manager() -> PriceManager:
    return PriceManager(
        x_price_source=StubXPriceSource(return_result=Decimal("150.00")),
        y_price_source=StubYPriceSource(return_result=Decimal("200.00"))
    )

class TestPriceManager:
    """
    pytest will complete the required dependencies during test (DI)
    """
    def test_get_price_if_product_type_eq_x(self, price_manger: PriceManager) -> None:
        product = Product(type="x")

        got = price_manger.get_price(product)

        assert got == Decimal("150.00")