from django.urls import path
from .views import index, contato, produto

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),  # a barra / é opcional
    path('produto/', produto, name='produto'),  # a barra / é opcional
]