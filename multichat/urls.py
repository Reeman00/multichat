from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from chat.views import index

urlpatterns = [
    path('', index),  # Home page or index
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),  # Updated login path
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
