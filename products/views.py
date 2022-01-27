from multiprocessing import context
from django.shortcuts import render

import pandas as pd

from .models import Product, Purchase

# Create your views here.


def chart_select_view(request):
    product_df = pd.DataFrame(Product.objects.all().values())
    purchase_df = pd.DataFrame(Purchase.objects.all().values())
    context = {
        'products': product_df.to_html(),
        'purchase': purchase_df.to_html(),
    }
    return render(request, 'products/main.html', context)