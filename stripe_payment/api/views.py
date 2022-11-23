from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from api.models import Item
from stripe_payment.settings import STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY
import stripe 


def get_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    context = {
        'item': item,
        'public_key': STRIPE_PUBLIC_KEY,
    }
    return render(request, 'base.html', context)

def buy_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    stripe.api_key = STRIPE_SECRET_KEY
    product = stripe.Product.create(
        name=item.name,
        description=item.description,
    )
    price = stripe.Price.create(
        unit_amount=item.price*100,
        currency='usd',
        product=product.get('id')
    )
    session = stripe.checkout.Session.create(
        success_url='http://localhost:8000/success',
        cancel_url='http://localhost:8000/cancel',
        line_items=[
            {
                'price': price.get('id'),
                'quantity': 1,
            },
        ],
        mode='payment',
    )
    print(session)
    return JsonResponse(session)