"""URLs do app postos. Cada path liga uma URL a uma view."""
from django.contrib import admin
from django.urls import path, include
from home import views
"""from . import views"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home)
     # Quando a URL nao for /admin, manda pro app postos
    #path('', include('postos.urls')), #isso tá na primeira parte do projeto
    """path('', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
    path('posto/<int:posto_id>/', views.detalhes_view, name='detalhes'),
    path('perfil/', views.perfil_view, name='perfil'),
"""
]