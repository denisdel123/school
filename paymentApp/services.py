import requests
import stripe
from rest_framework import status

from app import settings

stripe.api_key = settings.STRIPE_API_KEY
CURRENCY_API_KEY = settings.CURRENCY_API_KEY


def convert_rub_to_usd(amount):
    """Конвертирует рубль в доллар."""
    usd = 0
    link = f'https://api.currencyapi.com/v3/latest?apikey={CURRENCY_API_KEY}&currencies=RUB'

    response = requests.get(link)
    if response.status_code == status.HTTP_200_OK:
        currency = response.json()['data']['RUB']['value']
        usd = int(amount / currency)

    return usd


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
