import stripe
from forex_python.converter import CurrencyRates

from app import settings

stripe.api_key = settings.STRIPE_API_KEY


def convert_rub_to_usd(amount):
    """Конвертирует рубль в доллар."""
    # currency = CurrencyRates()
    # rate = currency.get_rate('RUB', 'USD')

    return int(amount / 91)


def create_stripe_product(name):
    """Создание продукта."""
    product = stripe.Product.create(name=name)
    return product.id


def create_stripe_price(amount, product_name):
    """Создание стоимости."""
    product_id = create_stripe_product(product_name)
    price = stripe.Price.create(
        currency="usd",
        unit_amount=amount * 100,
        product=product_id,
    )
    return price


def create_stripe_session(price):
    """Создание сессии на оплату."""
    session = stripe.checkout.Session.create(
        success_url="https://127.0.0.1:8000/",
        line_items=[
            {
                "price": price.get("id"),
                "quantity": 1
            }
        ],
        mode="payment",
    )
    return session.get("id"), session.get("url")
