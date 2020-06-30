from django.urls import path
from . import views as store_views

urlpatterns = [
    path('store/', store_views.SerwMedStore.store, name='serw-med-store'),
    path('cart/', store_views.SerwMedStore.cart, name='serw-med-cart'),
    path('checkout/', store_views.SerwMedStore.checkout, name='serw-med-checkout'),
    path('store/<int:pk>/', store_views.SerwMedStoreProduct.as_view(), name='serw-med-product'),
    path('update-item/', store_views.SerwMedStore.updateItem, name='serw-med-update-item'),
    path('process-order/', store_views.SerwMedStore.processOrder, name='serw-med-process-order'),
]