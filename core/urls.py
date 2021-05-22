from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import index, contato, produto

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),  # a barra / é opcional
    path('produto/', produto, name='produto'),  # a barra / é opcional
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)