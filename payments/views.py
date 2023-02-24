from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import stripe
from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


@csrf_exempt
def buy_item(request, id):
    item = Item.objects.get(pk=id)
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'unit_amount': int(item.price * 100),
                'product_data': {
                    'name': item.name,
                    'description': item.description
                },
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://localhost:8000/success?session_id={CHECKOUT_SESSION_ID}',
        cancel_url='http://localhost:8000/cancel',
    )
    return JsonResponse({'id': session.id})


def item_detail(request, id):
    item = Item.objects.get(pk=id)
    context = {
        'item': item,
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
    }
    return render(request, 'detail_item.html', context)
