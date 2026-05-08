from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('connexion/', auth_views.LoginView.as_view(template_name='membres/connexion.html'), name='connexion'),
    path('deconnexion/', auth_views.LogoutView.as_view(next_page='annuaire'), name='deconnexion'),
    path('', include('membres.urls')),
]
