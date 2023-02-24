from django.urls import path
from . import views

urlpatterns = [
    path('buy/<int:id>', views.buy_item),
    path('item/<int:id>', views.item_detail),
]
